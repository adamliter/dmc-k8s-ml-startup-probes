# -*- mode: python; coding: utf-8; fill-column: 88; -*-
from typing import Any

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.orjson.OrjsonFormatter",
            "format": """
        %(asctime)s
        %(levelname)s
        %(message)s
        %(module)s
        %(name)s
        """,
            "rename_fields": {
                "asctime": "@timestamp",
                "levelname": "level",
                "message": "msg",
            },
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "json": {
            "formatter": "json",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "dmc_k8s_ml_startup_probes": {
            "level": "INFO",
        },
        "uvicorn": {
            "level": "INFO",
        },
        "uvicorn.error": {
            "level": "INFO",
        },
        "uvicorn.asgi": {
            "level": "INFO",
        },
        "uvicorn.access": {
            "level": "WARNING",
        },
    },
    "root": {
        "level": "WARNING",
        "handlers": ["json"],
    },
}
