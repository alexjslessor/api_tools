#!/bin/bash
# source ./env.sh
# dev_env
# test_env

# uvicorn main:app --reload --port $PORT

run_tests() {
    py.test -s tests/four_chan/test_one.py
    # py.test -s tests/test_seed_collections.py
}
run_tests

build_container() {
    docker build -t data_tools:latest .  --network=host
    docker run \
            --name data_tools-container \
            -p $PORT:$PORT \
            --network=host \
            -e MONGO_DB_NAME=develop_db \
            -e AWS_REGION=ca-central-1 \
            -e AWS_S3_BUCKET= \
            -e AWS_S3_BUCKET= \
            -e WHICH_LOGGER=uvicorn \
            -e ENV_NAME=production \
            -e PORT=$PORT \
            data_tools:latest
}
# build_container

