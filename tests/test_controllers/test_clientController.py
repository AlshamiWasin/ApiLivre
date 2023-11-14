


# def test_get_user(client, monkeypatch):
#     # Assuming you have a Flask test client and you're using dependency injection (e.g., Flask-Injector)

#     # Mocking the service method
#     def mock_get_user(user_id):
#         return {'id': user_id, 'name': 'John Doe'}

#     monkeypatch.setattr(UserController, 'get_user_data', mock_get_user)

#     # Performing the request
#     response = client.get('/users/1')

#     # Asserting the response
#     assert response.status_code == 200
#     assert json.loads(response.data) == {'id': 1, 'name': 'John Doe'}