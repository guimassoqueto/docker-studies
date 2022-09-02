1. `docker build -t env:latest .`
2. `docker run --rm -it --name env -e TEST_ENV="TestEnv" --env-file ./.env_test env:latest bash`

Inside the container:
1. `echo $JACIR && echo $DIRCE && echo $GUILHERME && echo $TEST_ENV && echo $GUILLIAN`

Info tags:
`-e (or --env)` set the environment variable
`--env-file` set all the env variables of an .env file