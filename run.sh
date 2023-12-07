#!/bin/bash

# script for DPS algorithm.  
basedir=$( cd "$(dirname "$0")" ; pwd -P)

# create directory for the output. Used by src.py. 
mkdir -p "${PWD}/output"

python ${basedir}/src.py $1
