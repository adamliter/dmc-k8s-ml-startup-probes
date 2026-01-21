# Robust K8s ML Deployments with Startup Probes

This repo contains code for a talk, "Robust K8s ML Deployments with Startup
Probes", given at the at the [2026-01-22 Denver MLOps Community meetup][meetup].

## Environment setup

If you don't have `uv` installed, then:

``` sh
brew install uv
```

Then install the dependencies:

``` sh
uv sync --managed-python
```

Make sure that you also configure `pre-commit`:

``` sh
uv run pre-commit install
```

## Building the Docker image

``` sh
docker build -t dmc_k8s_ml_startup_probes:latest .
```


<!-- links -->
[meetup]: https://www.meetup.com/denver-mlops-community/events/312856102/
