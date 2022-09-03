#!/bin/bash

set_env() {
  BASE_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
  local env_file_path="$BASE_DIR/.env/$1"
  grep -v '^#' $env_file_path
  export $(grep -v '^#' $env_file_path | xargs)
  echo "<---ENV: $env_file_path --->"
}

dev_env() {
  set_env .base
  set_env .dev
  echo "${MONGO_DB_NAME}"
}
test_env() {
  set_env .base
  set_env .test
  echo "${MONGO_DB_NAME}"
}

