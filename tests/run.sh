#!/bin/bash
set -u
set -e

TEST_NUMBER=${TEST_NUMBER:-1}

docker-compose up -d --scale chrome=${TEST_NUMBER}
pytest --driver Remote --capability browserName chrome -n ${TEST_NUMBER} $@
docker-compose down
