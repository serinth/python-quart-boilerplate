# Production ready Python + Quart API Boilerplate
[ASGI](https://asgi.readthedocs.io/en/latest/introduction.html) compliant boilerplate code for a Python web API.
By referencing your Python classes, you'll be able to generate an OpenAPI specification automatically.

## Batteries included:
- CORS support
- OpenAPI specification with a Swagger UI
- Health check endpoint
- Redoc UI
- Docker support
- Helm Chart
- Secure headers on by default
- OpenTelemetry support
- Blueprint support to scale out your endpoints (same as Flask)
- A proper webserver instead of the framework one (which is not scalable or performant)

# Requirements

- [Poetry](https://python-poetry.org/)
- Python 3.11+

```bash
poetry config virtualenvs.in-project true
poetry install
curl localhost:8000/health
```

Included Helm Chart for CI/CD.
Default port is **8000** with hot reloading for DEV environment.

Hit http://localhost:8000/openapi.json for the specification or
http://localhost:8000/docs for the Swagger UI or
http://localhost:8000/redocs for the Redocs UI

# Environment Variables
|Variable|Description|Default|
|---	|---	|---	|
|WORK_ENV| DEV, STAGE, TEST, PROD|None -> Defaults to DEV|

# Running Tests

```bash
poetry run pytest
```

## Building the Docker image

1. Generate a requirements.txt from the lock file:
```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
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

## Key References
[Quart](https://quart.dev/)
[Quart-Schema](https://github.com/astral-sh/quart-schema)
[Hypercorn](https://pgjones.gitlab.io/hypercorn/)