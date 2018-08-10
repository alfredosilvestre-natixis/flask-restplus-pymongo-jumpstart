import pytest

import app


@pytest.fixture
def client():
    application = app.App()
    client = application.create_app(flask_config_name='testing').test_client()

    yield client

