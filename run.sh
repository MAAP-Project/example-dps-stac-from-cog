#!/bin/bash
# script for DPS algorithm.  

env

basedir=$( cd "$(dirname "$0")" ; pwd -P)

# create directory for the output. Used below for output. 
mkdir -p "${PWD}/output"

# produce the STAC item 
rio stac $1 --output output/item.json