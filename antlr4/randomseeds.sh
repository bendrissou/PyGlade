#!/bin/bash

#How many random files to be pulled
random_file_size=1500

#read from source file and randomly populate images
images=(lua/generate/random/*)

i=0
while [ ${i} -le ${random_file_size} ]
do
    cp ${images[RANDOM % ${#images[@]}]} lua/generate/lua
    ((i++))
done
