from flask import Blueprint , request , jsonify
from services.ServiceCommande import ServiceCommande


# Create the auth app
commande = Blueprint('commande', __name__)
serviceCommande = ServiceCommande

# Define the routes
@commande.route('/commandes' , methods=['GET'])
def getCommands():
    commandes = serviceCommande.getAllCommande()
    serialized_commandes = [commande.serialize() for commande in commandes]
    return jsonify(serialized_commandes)
    
    return 


''' POST
Créer un nouveau commande dans la BDD
'''
@commande.route('/commande' , methods=['POST'])
def createClient():
    data = request.json

    idClient = data.get('idClient')
    idOuvrage = data.get('idOuvrage')
    idMP = data.get('idMP')
    montant = data.get('montant')

    if idClient and idOuvrage and idMP and montant:
        client = serviceCommande.createCommand(idClient, 
                                      idOuvrage,
                                      idMP,
                                      montant)
        # return jsonify(user.serialize)
        return jsonify(client.serialize()), 200 
    else:
        return jsonify({'message': 'Invalid input'}), 400


@commande.route('/commands/<int:command_id>', methods=['GET'])
def getCommand(command_id):
    command = serviceCommande.getCommandById(command_id)
    if command:
        return jsonify(command.serialize()) , 200
    else:
        return jsonify({"error": "Command not found"}), 404
    
@commande.route('/commands/<int:command_id>', methods=['PUT'])
def updateCommand(command_id):
    data = request.get_json()
    updatedCommand = serviceCommande.updateCommand(command_id, data)
    if updatedCommand:
        return jsonify(updatedCommand.serialize()) , 200
    else:
        return jsonify({"error": "Command not found"}), 404
    
@commande.route('/commands/<int:command_id>', methods=['DELETE'])
def delete_command(command_id):
    success = serviceCommande.deleteCommand(command_id)
    if success:
        return jsonify({"message": "Command deleted successfully"}), 200
    else:
        return jsonify({"error": "Command not found"}), 404