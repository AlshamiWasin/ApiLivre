from flask import Blueprint , request , jsonify
from services.ServiceMoyenPaiement import ServiceMoyenPaiement

# Create the auth app
moyenpaiement = Blueprint('moyenpaiement', __name__)
serviceMoyenPaiement = ServiceMoyenPaiement


# Define the routes
@moyenpaiement.route('/moyenpaiements' , methods=['GET'])
def getMoyenPaiements():
    return serviceMoyenPaiement.getAllMoyenPaiements()
    

# Define the Routes
@moyenpaiement.route('/moyenpaiement/<int:id_moyenpaiement>' , methods=['GET'])
def getMoyenPaiementById(id_moyenpaiement):
    moyenpaiement = serviceMoyenPaiement.getMoyenPaiementById(id_moyenpaiement)
    if moyenpaiement:
        return jsonify(moyenpaiement.serialize()), 200 
    else:
        return jsonify({'message': 'MoyenPaiement not found'}), 400


''' POST
Créer un nouveau moyenpaiement dans la BDD
'''
@moyenpaiement.route('/moyenpaiement' , methods=['POST'])
def createMoyenPaiement():
    data = request.json

    type = data.get('type_paiement')
    nom = data.get('nom_proprietaire_paiement')
    numero = data.get('numero_moyen_paiement')
    date = data.get('date_expiration_paiement')
    code = data.get('code_secu_paiement')


    if type and nom and numero and date and code:
        moyenpaiement = serviceMoyenPaiement.createMoyenPaiement(type , 
                                      nom ,
                                      numero,
                                      date, 
                                      code)
        # return jsonify(user.serialize)
        return jsonify(moyenpaiement.serialize()), 200 
    else:
        return jsonify({'message': 'Invalid input'}), 400

@moyenpaiement.route('/moyenpaiement/<int:moyenpaiement_id>', methods=['PUT'])
def updateMoyenPaiement(moyenpaiement_id):
    data = request.json
    new_type = data.get('type_paiement')
    new_nom = data.get('nom_proprietaire_paiement')
    new_numero = data.get('numero_moyen_paiement')
    new_date = data.get('date_expiration_paiement')
    new_code = data.get('code_secu_paiement')

    if new_type and new_nom and new_numero and new_date and new_code:
        updated_moyenpaiement = serviceMoyenPaiement.updateMoyenPaiement(moyenpaiement_id, new_type, new_nom, new_numero , new_date, new_code)
        if updated_moyenpaiement:
            return jsonify(updated_moyenpaiement.serialize()), 200 
        else:
            return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'message': 'Invalid input'}), 400
    

@moyenpaiement.route('/moyenpaiement/<int:moyenpaiement_id>', methods=['DELETE'])
def deleteMoyenPaiement(moyenpaiement_id):
    success = serviceMoyenPaiement.deleteMoyenPaiement(moyenpaiement_id)
    if success:
        return jsonify({'message': 'MoyenPaiement deleted successfully'}), 200 
    else:
        return jsonify({'message': 'MoyenPaiement not found'}), 404