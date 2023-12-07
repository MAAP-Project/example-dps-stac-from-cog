# Example of STAC item creation in a DPS algorithm

This repository stores code for an example MAAP DPS algorithm that produces STAC metadata from a Cloud Optimized Geotiff file. For the purpose of providing an example, the data isn't processed at all and we are just downloading an already existing COG from a public S3 location provided by the user. 

STAC item creation from the COG is automated using `rio-stac`.

## Structure

- `src.py` contains the python module in itself that downloads the file. 
- `requirements.txt` lists the required python dependencies. 
- `run.sh` see DPS usage below.
- `algorithm_config.yml` see DPS usage below. 
- `job_config.yml` see DPS usage below.
- `register_and_run.ipynb` see DPS usage below. 

## Requirements

- python >=3.10
- `requirements.txt`
- authenticated to an AWS account.

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

Please make sure your AWS credentials are set up before running this command. 

```
python download.py --download_from s3://sentinel-cogs/sentinel-s2-l2a-cogs/51/U/WR/2023/12/S2A_51UWR_20231207_0_L2A/TCI.tif --download_to /tmp/downloaded.tiff
```

 ## DPS usage

You can refer to the YAML files and the notebook in this repository to see what algorithm is registered and its configuration, or re-register it yourself. 

- `algorithm_config.yml` config for registering the algorithm to the MAAP platform.
- `job_config.yml` config for submitting a job with the algoritum to the MAAP platform.
- `register_and_run.ipynb` example commands to programmatically register the algorithm and submit a job. 

And `run.sh` is the bash script that runs `src.py` and is an entrypoint required for a DPS algorithm.

### Discover output in DPS

This algorithm stores the two following files in the output folder of the DPS job : 

- the STAC item in JSON format
- the downloaded tiff