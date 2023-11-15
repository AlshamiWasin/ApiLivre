from flask import Blueprint , request , jsonify
from services.ServiceClient import ServiceClient

# Create the auth app
client = Blueprint('client', __name__)
serviceClient = ServiceClient

''' GET
Récupérer tous les clients
'''
# Define the routes
@client.route('/clients' , methods=['GET'])
def getClients():
    # swagger
    """
    Get : Liste des clients
    ---

    responses:
      200:
        description: Liste des clients.
    """
    clients = serviceClient.getAllClients()
    serialized_clients = [client.serializeFull() for client in clients] #serializedFull pour récupérer aussi l'ID.
    return jsonify(serialized_clients)
    

''' GET
Récupérer un client par son ID
'''
# Define the Routes
@client.route('/client/<int:id_client>' , methods=['GET'])
def getClientById(id_client):
    # swagger
    """
    Get : Un client par son ID
    ---
    
    parameters:
      -  name: id_client
         in: path
         required: true
         schema:
           type : integer
    responses:
      200:
        description: Client found
      400:
        description: Client not found
    """
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
    # swagger
    """
    Post : Ajouter un nouveau client
    ---

    responses:
      200:
        description: Client ajouté
      400:
        description: Client non ajouté
    """  
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


''' PUT
Update d'un client par son ID
'''
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
    

''' DELETE
Supprimer un client par son ID
''' 
@client.route('/client/<int:client_id>', methods=['DELETE'])
def deleteClient(client_id):
    success = serviceClient.deleteClient(client_id)
    if success:
        return jsonify({'message': 'Client deleted successfully'}), 200 
    else:
        return jsonify({'message': 'Client not found'}), 404