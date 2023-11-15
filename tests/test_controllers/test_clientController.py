import json
import pytest
from tests.test_conf.FakeApp import create_app

@pytest.fixture
def client():
    # Implement your Flask app creation logic here
    app = create_app()
    with app.test_client() as client:
        yield client


def test_get_client(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Performing the request
    response = client.get('/client/2')

    # Asserting the response
    assert response.status_code == 200
    assert json.loads(response.data) == {
                                            "email_client": "updated@email.com",
                                            "nom_client": "last Name",
                                            "prenom_client": "first Name",
                                            "telephone_client": "0123456789"
                                        }
    

def test_dont_get_client(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Performing the request
    response = client.get('/client/99999')

    # Asserting the response
    assert response.status_code == 400


def test_update_client_good_data(client, monkeypatch):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Mocking the service method
    # def mock_update_client(client_id, new_nom, new_prenom , new_email, new_tel):
    #     return {'nom': 'last Name', 'email': 'updated@email.com',
    #                'prenom': 'first Name', 'tel': '0123456789'}

    # monkeypatch.setattr(ServiceClient, 'updateClient', mock_update_client)

    update_data = {'nom': 'last Name', 'email': 'updated@email.com',
                   'prenom': 'first Name', 'tel': '0123456789'}
    # Performing the request
    response = client.put('/client/2', json=update_data)

    # Asserting the response
    assert response.status_code == 200