from flask import Blueprint , request , jsonify
from services.ServiceOuvrage import ServiceOuvrage

# Create the auth app
ouvrage = Blueprint('ouvrage', __name__)
serviceOuvrage = ServiceOuvrage


''' GET
Récupérer tous les ouvrages
'''
# Define the route
@ouvrage.route('/ouvrages' , methods=['GET'])
def getAllOuvrages():
    ouvrages = serviceOuvrage.getAllOuvrages()
    # transformer le résultat en liste JSON
    serialized_ouvrages = [ouvrage.serialize() for ouvrage in ouvrages]
    return jsonify(serialized_ouvrages)


''' GET
Récupérer un ouvrage par son ID
'''
# Define the route
@ouvrage.route('/ouvrage/<int:id_ouvrage>' , methods=['GET'])
def getOuvrageById(id_ouvrage):
    ouvrage = serviceOuvrage.getOuvrageById(id_ouvrage)
    if ouvrage:     #Si l'ouvrage est trouvé
        return jsonify(ouvrage.serialize()), 200 
    else:
        return jsonify({'message': 'Ouvrage not found'}), 400


''' POST
Créer un nouvel ouvrage dans la BDD
Avec en paramètres seulement titre et auteur
Utile pour tester rapidement !
'''
@ouvrage.route('/ouvrageTitreAuteur' , methods=['POST'])
def createOuvrageTitreAuteur():
    data = request.json

    titre = data.get('titre')
    auteur = data.get('auteur')

    if titre and auteur:
        ouvrage = serviceOuvrage.createOuvrageTitreAuteur(data.get('titre') , 
                                      data.get('auteur'))
        return jsonify(ouvrage.serialize()), 200
    else:
        return jsonify({'message': 'Invalid input'}), 400


''' POST
Créer un nouvel ouvrage dans la BDD
Avec tous les paramètres
'''
@ouvrage.route('/ouvrage' , methods=['POST'])
def createOuvrage():
    data = request.json

    titre = data.get('titre')
    auteur = data.get('auteur')
    isbn = data.get('isbn')
    langue = data.get('langue')
    prix = data.get('prix')
    date = data.get('date')
    categorie = data.get('categorie')
    date_disponibilite_libraire = data.get('date_disponibilite_libraire')
    date_disponibilite_particulier = data.get('date_disponibilite_particulier')
    image = data.get('image')
    table_des_matieres = data.get('table_des_matieres')
    date_parution = data.get('date_parution')
    mot_cle = data.get('mot_cle')
    description = data.get('description')

    # paramètres obligatoires
    if titre and auteur and isbn :
        ouvrage = serviceOuvrage.createOuvrage(data.get('titre'), 
                                      data.get('auteur'),
                                      data.get('isbn'),
                                      data.get('langue'),
                                      data.get('prix'),
                                      data.get('date_parution'),
                                      data.get('date'),
                                      data.get('categorie'),
                                      data.get('date_disponibilite_libraire'),
                                      data.get('date_disponibilite_particulier'),
                                      data.get('image'),
                                      data.get('table_des_matieres'),
                                      data.get('mot_cle'),
                                      data.get('description')
                                      )
        return jsonify(ouvrage.serialize()), 200
    else:
        return jsonify({'message': 'Invalid input'}), 400


# @client.route('/client/<int:client_id>', methods=['PUT'])
# def updateClient(client_id):
#     data = request.json
#     new_nom = data.get('nom')
#     new_prenom = data.get('prenom')
#     new_email = data.get('email')
#     new_tel = data.get('tel')

#     if new_nom and new_prenom and new_email and new_tel:
#         updated_client = serviceClient.updateClient(client_id, new_nom, new_prenom , new_email, new_tel)
#         if updated_client:
#             return jsonify(updated_client.serialize()), 200 
#         else:
#             return jsonify({'message': 'User not found'}), 404
#     else:
#         return jsonify({'message': 'Invalid input'}), 400
    

# @client.route('/client/<int:client_id>', methods=['DELETE'])
# def deleteClient(client_id):
#     success = serviceClient.deleteClient(client_id)
#     if success:
#         return jsonify({'message': 'Client deleted successfully'}), 200 
#     else:
#         return jsonify({'message': 'Client not found'}), 404