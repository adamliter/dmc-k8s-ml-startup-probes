# -*- mode: python; coding: utf-8; fill-column: 88; -*-
from fastapi.testclient import TestClient

from dmc_k8s_ml_startup_probes.app.main import MODEL_NAME, app


def test_predict_returns_200():
    with TestClient(app) as client:
        response = client.get(f"/api/v1/{MODEL_NAME}")

    assert response.status_code == 200

    assert MODEL_NAME in response.json()
