#!/bin/bash
# script for DPS algorithm.  


basedir=$( cd "$(dirname "$0")" ; pwd -P)

# create directory for the output. Used below for output. 
mkdir -p "${PWD}/output"

# download the COG
python ${basedir}/download.py $1 output/downloaded.tiff

# produce the STAC item 
rio stac output/downloaded.tiff --output output/item.json