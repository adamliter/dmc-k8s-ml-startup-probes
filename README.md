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

## Following along

1. Ensure you have all necessary dependencies installed:

    - Docker (if on a Mac, you can, for example, install [Docker
      Desktop][mac-docker])
    - `k3d`: `brew install k3d`
    - `kubectl`: `brew install kubernetes-cli`

1. Clone the repo:

   ```sh
   git clone https://github.com/adamliter/dmc-k8s-ml-startup-probes.git
   ```

1. Build the docker image for the FastAPI toy app in this repo:

   ```sh
   cd dmc-k8s-ml-startup-probes
   docker build -t dmc_k8s_ml_startup_probes:latest .
   ```

1. Create a K8s cluster named `mlops` that runs inside Docker and is configured
   to use the local Docker host as a Docker registry (via
   [`k3d-registry-dockerd`][k3d-registry-dockerd]):

   ```sh
   configfile=$(mktemp)
   cat << HERE > "$configfile"
   apiVersion: k3d.io/v1alpha5
   kind: Simple
   registries:
     create:
       image: ligfx/k3d-registry-dockerd:latest
       proxy:
         remoteURL: "*"
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock
   HERE
   k3d cluster create mlops --config "$configfile"
   ```


<!-- links -->
[meetup]: https://www.meetup.com/denver-mlops-community/events/312856102/
[mac-docker]: https://docs.docker.com/desktop/setup/install/mac-install/
[k3d-registry-dockerd]: https://github.com/ligfx/k3d-registry-dockerd
