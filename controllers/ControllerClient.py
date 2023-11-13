from flask import Blueprint , request , jsonify
from services.ServiceClient import ServiceClient

# Create the auth app
client = Blueprint('client', __name__)
serviceClient = ServiceClient


# Define the routes
@client.route('/clients' , methods=['GET'])
def getClients():
    clients = serviceClient.getAllClients()
    serialized_clients = [client.serialize() for client in clients]
    return jsonify(serialized_clients)
    

# Define the Routes
@client.route('/client/<int:id_client>' , methods=['GET'])
def getClientById(id_client):
    client = serviceClient.getClientById(id_client)
    if client:
        return jsonify(client.serialize()), 200 
    else:
        return jsonify({'message': 'Client not found'}), 400


''' POST
Créer un nouveau client dans la BDD
'''
@client.route('/client' , methods=['POST'])
def createClient():
    data = request.json

    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    tel = data.get('tel')

    if nom and prenom and email and tel:
        client = serviceClient.createClient(nom , 
                                      prenom,
                                      email,
                                      tel)
        # return jsonify(user.serialize)
        return jsonify(client.serialize()), 200 
    else:
        return jsonify({'message': 'Invalid input'}), 400

@client.route('/client/<int:client_id>', methods=['PUT'])
def updateClient(client_id):
    data = request.json
    new_nom = data.get('nom')
    new_prenom = data.get('prenom')
    new_email = data.get('email')
    new_tel = data.get('tel')

    if new_nom and new_prenom and new_email and new_tel:
        updated_client = serviceClient.updateClient(client_id, new_nom, new_prenom , new_email, new_tel)
        if updated_client:
            return jsonify(updated_client.serialize()), 200 
        else:
            return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'message': 'Invalid input'}), 400
    

@client.route('/client/<int:client_id>', methods=['DELETE'])
def deleteClient(client_id):
    success = serviceClient.deleteClient(client_id)
    if success:
        return jsonify({'message': 'Client deleted successfully'}), 200 
    else:
        return jsonify({'message': 'Client not found'}), 404