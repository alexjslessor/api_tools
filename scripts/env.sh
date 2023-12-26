#!/bin/bash

set_env() {
  local env_file_path="$1"
  grep -v '^#' $env_file_path
  export $(grep -v '^#' $env_file_path | xargs)
  echo "<---ENV: $env_file_path --->"
}

dev_env_lib() {
  set_env .env/.base
#   set_env .env/.base.360
  echo "${MONGO_DB_NAME}"
}

