# Python + Quart API Boilerplate

# Requirements
Python 3.9+

```bash
pipenv install
pipenv run python src/server.py
curl localhost:8000/health
```

Included Helm Chart for CI/CD.
Default port is **8000** with hot reloading for DEV environment.

Hit localhost:8000/openapi.json for the specification

# Environment Variables
|Variable|Description|Default|
|---	|---	|---	|
|WORK_ENV| DEV, STAGE, TEST, PROD|None -> Defaults to DEV|

# Running Tests

```bash
pipenv run nose2
```

## Building the Docker image

1. Generate a requirements.txt from the lock file:
```bash
pipenv lock -r > requirements.txt
```

2. Build the docker image
```bash
docker build -t mydomain.com/myimage:latest .
```

3. Running
```bash
docker run \
-e WORK_ENV="PROD" \
-p 8000:8000 \
mydomain.com/myimage:latest
```