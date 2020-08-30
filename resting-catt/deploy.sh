#!/bin/bash
git pull; git reset --hard origin/master; docker build --tag carlba/resting-catt:0.0.1a10 .;  docker push carlba/resting-catt:0.0.1a10
