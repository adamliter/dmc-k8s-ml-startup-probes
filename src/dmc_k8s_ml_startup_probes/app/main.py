# -*- mode: python; coding: utf-8; fill-column: 88; -*-
import logging
from contextlib import asynccontextmanager
from random import randint
from time import sleep, time

from fastapi import FastAPI

_logger = logging.getLogger(__name__)

MODEL_NAME: str = "my-model"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.models = {}

    _logger.info("Loading model at application startup.")
    st: float = time()

    app.state.models[MODEL_NAME] = "is the best"
    sleep(randint(59, 85))

    _logger.info("Finished loading model after %(t)d seconds.", {"t": int(time() - st)})

    yield

    app.state.models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/healthz")
async def healthz():
    return {"status": "live"}


@app.get("/readyz")
async def readyz():
    return {"status": "ready"}


@app.get(f"/api/v1/{MODEL_NAME}")
async def predict():
    return {MODEL_NAME: app.state.models[MODEL_NAME]}


def main(app: "FastAPI" = app) -> None:
    import argparse
    from logging import captureWarnings

    import uvicorn

    from . import LOGGING_CONFIG

    captureWarnings(True)
    logging.basicConfig(level="INFO")

    parser = argparse.ArgumentParser(
        description="Toy FastAPI app for demonstrating startup probes"
    )
    parser.add_argument(
        "--port", dest="port", default=8080, help="The port to run the server on."
    )
    parser.add_argument(
        "--host",
        dest="host",
        default="0.0.0.0",
        help="The host address for the server.",
    )

    args = parser.parse_args()

    uvicorn.run(
        app, host=str(args.host), port=int(args.port), log_config=LOGGING_CONFIG
    )
