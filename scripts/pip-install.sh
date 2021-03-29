#!/bin/bash

docker-compose exec py /bin/bash -c "pip install $1 && pip freeze > requirements.txt"
