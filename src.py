import sys

import boto3
import fsspec
import h5py
import rioxarray

SSM_PARAMETER_NAME = "/iam/maap-data-reader"
OUTPUT_FILE_PATH = 'output/output_message.txt'

def s3_access(ssm_parameter_name: str) -> fsspec.filesystem:
    """
    Assume role stored in ssm parameter and return s3 filesystem object
    with session credentials based on role
    """
    
    print(f'retrieving credentials from role in {ssm_parameter_name} ssm parameter')

    session = boto3.Session()

    # Retrieve the SSM parameter
    ssm = session.client("ssm", "us-west-2")
    parameter = ssm.get_parameter(Name=ssm_parameter_name, WithDecryption=True)
    parameter_value = parameter["Parameter"]["Value"]

    # Assume the new role
    sts = session.client("sts")
    assumed_role_object = sts.assume_role(
        RoleArn=parameter_value, RoleSessionName="TutorialSession"
    )

    # From the response that contains the assumed role, get the temporary
    # credentials that can be used to make subsequent API calls
    credentials = assumed_role_object["Credentials"]


    fs = fsspec.filesystem(
        "s3",
        key=credentials["AccessKeyId"],
        secret=credentials["SecretAccessKey"],
        token=credentials["SessionToken"],
    )
    
    print('done retrieving credentials')
    return fs


def read_file(s3_path, ssm_parameter_name=SSM_PARAMETER_NAME):
    
    """
    accepts only .tif or 
    """
    s3 = s3_access(ssm_parameter_name)
    print(f"accessing {s3_path}")
    with s3.open(s3_path) as obj:
        if s3_path.endswith(".tif"):
            rioxarray.open_rasterio(obj)
        elif s3_path.endswith(".h5"):
            h5py.File(obj, "r")
        else:
            print("File type not supported")
    print(f"accessed {s3_path}")
    with open(OUTPUT_FILE_PATH, 'w') as f:
        f.write(f"accessed {s3_path}")


if __name__ == "__main__":
    read_file(sys.argv[1])
