from flask import Blueprint , request , jsonify
from services.ServiceClient import ServiceClient

# Create the auth app
client = Blueprint('client', __name__)
serviceClient = ServiceClient


# Define the Rotues
@client.route('/clients' , methods=['GET'])
def getClients():
    return serviceClient.getAllClients()
    

# Define the Rotues
@client.route('/client/<int:id_client>' , methods=['GET'])
def getClientById(id_client):
    client = serviceClient.getClientById(id_client)
    if client:
        return jsonify(client.serialize()), 200 
    else:
        return jsonify({'message': 'Client not found'}), 400


@client.route('/client' , methods=['POST'])
def createClient():
    data = request.json

    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    tel = data.get('tel')

    if nom and prenom and email and tel:
        client = serviceClient.createClient(data.get('nom') , 
                                      data.get('prenom') ,
                                      data.get('email') ,
                                      data.get('tel'))
        # return jsonify(user.serialize)
        return jsonify(client.serialize()), 200 
    else:
        return jsonify({'message': 'Invalid input'}), 400