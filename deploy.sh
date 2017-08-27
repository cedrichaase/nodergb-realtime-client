#!/usr/bin/env bash

HOST=192.168.178.2

project_folder=${PWD##*/}

rsync -avr --delete --exclude .git --exclude .idea --exclude deploy.sh --exclude '*.pyc' --exclude __pycache__ . pi@${HOST}:${project_folder}
