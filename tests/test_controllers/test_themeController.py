import json
import pytest
from tests.test_conf.FakeApp import create_app


@pytest.fixture
def client():
    # Implement your Flask app creation logic here
    app = create_app()
    with app.test_client() as client:
        yield client



def test_get_themes(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Performing the request
    response = client.get('/themes')

    # Asserting the response
    assert response.status_code == 200


def test_get_theme_by_id(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Performing the request
    response = client.get('/theme/1')

    # Asserting the response
    assert response.status_code == 400



def test_update_theme_by_id(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Performing the request
    response = client.get('/theme/1')

    # Asserting the response
    assert response.status_code == 400