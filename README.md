# Example of AWS S3 access to DAAC buckets in MAAP DPS

This repository stores code for an example MAAP DPS algorithm that provides an example for two tasks : 
- most importantly, the algorithm test AWS S3 DAAC buckets access by reading tiff or hdf5 files stored in these buckets. Access in this module relies on retrieving temporary credentials from the `maap-data-reader` role which was created for multi-DAAC access, and pass these credentials to the filesystem python client `fs` (which relies on `s3fs` for AWS S3).
- the algorithm also provides an example of how to generate and discover DPS output. 

## Structure

- `src.py` contains the python module in itself.
- `requirements.txt` lists the required python dependencies. 
- `run.sh` see DPS usage below.
- `algorithm_config.yml` see DPS usage below. 
- `job_config.yml` see DPS usage below.
- `register_and_run.ipynb` see DPS usage below. 

## Requirements

- python >=3.10
- `requirements.txt`
- authenticated to an AWS account and user with permissions to assume the `maap-data-reader` role. 

## Local usage

### Installation

From the root of this repository :

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

or if you are in a conda environment, you can directly update it with 

```
pip install -r requirements.txt
```

### Usage

Here are a few examples of usage of the module, each example using a different DAAC bucket. From the root of the repository after the installation step : 

```
# NSIDC DAAC Access
python src.py s3://nsidc-cumulus-prod-protected/ATLAS/ATL08/006/2023/06/21/ATL08_20230621235543_00272011_006_01.h5

# ORNL DAAC Access
python src.py s3://ornl-cumulus-prod-protected/gedi/GEDI_L4B_Gridded_Biomass/data/GEDI04_B_MW019MW138_02_002_05_R01000M_PS.tif

# GES DISC Access
python src.py s3://gesdisc-cumulus-prod-protected/Landslide/Global_Landslide_Nowcast.1.1/2020/Global_Landslide_Nowcast_v1.1_20201231.tif

# LP DAAC Access
python src.py s3://lp-prod-protected/HLSL30.020/HLS.L30.T56JMN.2023225T234225.v2.0/HLS.L30.T56JMN.2023225T234225.v2.0.B11.tif
 ```

 ## DPS usage

You can refer to the YAML files and the notebook in this repository to see what algorithm is registered and its configuration, or re-register it yourself. 

- `algorithm_config.yml` config for registering the algorithm to the MAAP platform.
- `job_config.yml` config for submitting a job with the algoritum to the MAAP platform.
- `register_and_run.ipynb` example commands to programmatically register the algorithm and submit a job. 

And `run.sh` is the bash script that runs `src.py` and is an entrypoint required for a DPS algorithm.

### Discover output in DPS

This algorithm creates a text file at the path described in `src.OUTPUT_FILE_PATH`. The purpose is to show how output is handled in a DPS job. The algorithm just writes a 'job succeeded' type of message in the text file, and, after a sucessful job, this text file can be found in a MAAP user's private bucket, in `dps_output`. 