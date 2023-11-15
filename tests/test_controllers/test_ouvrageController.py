import json
import pytest
from tests.test_conf.FakeApp import create_app


@pytest.fixture
def client():
    # Implement your Flask app creation logic here
    app = create_app()
    with app.test_client() as client:
        yield client


def test_get_ouvrages(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Performing the request
    response = client.get('/ouvrages')

    # Asserting the response
    assert response.status_code == 200



def test_get_ouvrage_by_id(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    # Performing the request
    response = client.get('/ouvrage/1')

    # Asserting the response
    assert response.status_code == 200


def test_create_ouvrage(client):
    # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

    data = {
        "titre":"Mon titre test 2",
        "auteur":"Mon auteur test 2",
        "isbn":"2-7654-1005-4",
        "langue":"fr",
        "prix":"0",
        "date_parution":None,
        "categorie":"BD",
        "date_disponibilite_libraire":None,
        "date_disponibilite_particulier":None,
        "image":"mon_image",
        "table_des_matieres":"lalala",
        "mot_cle":"cool",
        "description":"cool"
    } 

    # Performing the request
    response = client.post('/ouvrage', json=data)

    # Asserting the response
    assert response.status_code == 200