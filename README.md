# Example of STAC item creation in a DPS algorithm

This repository stores code defining an example MAAP DPS algorithm that scans (without downloading it) a COG stored in S3 to produce STAC metadata out of it and save that STAC record locally. 

## Structure

See "DPS usage" below for details about the following. 

- `run.sh`
- `build.sh`
- `algorithm_config.yml`
- `job_config.yml`
- `register_and_run.ipynb`

## Requirements

- python >=3.10
- `rio-stac` (used to automate the STAC metadata creation and S3 I/O)
- authenticated to an AWS account.

## Local usage

### Installation

From the root of this repository :

```
python -m venv .venv
source .venv/bin/activate
pip install rio-stac==0.8.1
```

or if you are in a conda environment, you can directly update it with 

```
pip install rio-stac==0.8.1
```

### Usage

Please make sure your AWS credentials are set up before running this command. 

```
rio stac s3://sentinel-cogs/sentinel-s2-l2a-cogs/51/U/WR/2023/12/S2A_51UWR_20231207_0_L2A/TCI.tif --output /tmp/item.json
```

 ## DPS usage

You can refer to the YAML files and the notebook in this repository to see what algorithm is registered and its configuration, or re-register it yourself. 

- `algorithm_config.yml` config for registering the algorithm to the MAAP platform.
- `job_config.yml` config for submitting a job with the algoritum to the MAAP platform.
- `register_and_run.ipynb` example commands to programmatically register the algorithm and submit a job. 

And `run.sh` is the bash script that runs the STAC creation command. 

### Discover output in DPS

This algorithm stores the STAC metadata file in the output folder of the DPS job.