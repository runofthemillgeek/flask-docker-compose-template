# Flask + Docker Compose for Development

## Requirements

- Docker Desktop

## Instructions

```sh
./scripts/dev.sh
```

This will build the image from `Dockerfile.dev` and start the server watching .py/.json files using nodemon.

Ctrl + C will quit the server and stop the container.

If you need to force rebuild the image, in case you modified `Dockerfile.dev`, run:

```sh
./scripts/devbuild.sh
```

## pip install

Ensure dev environment is up by running `./scripts/dev.sh` and then run the following:

```sh
./scripts/pip-install requests
```

This will run using `docker-compose exec` so it'll also update the local `requirements.txt` and restart nodemon.
