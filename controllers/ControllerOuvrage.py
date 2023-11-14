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
Paramètres : titre, auteur
'''
@ouvrage.route('/ouvrageTitreAuteur' , methods=['POST'])
def createOuvrageTitreAuteur():
    # récupération des données
    data = request.json

    #récupération des attributs
    titre = data.get('titre')
    auteur = data.get('auteur')

    #si les attributs sont bien récupérés
    if titre and auteur:
        ouvrage = serviceOuvrage.createOuvrageTitreAuteur(titre, 
                                      auteur)
        return jsonify(ouvrage.serialize()), 200
    else:
        return jsonify({'message': 'Invalid input'}), 400


''' POST
Créer un nouvel ouvrage dans la BDD
Avec tous les paramètres
'''
@ouvrage.route('/ouvrage' , methods=['POST'])
def createOuvrage():
    #récupération des données
    data = request.json

    #récupération des attributs
    titre = data.get('titre')
    auteur = data.get('auteur')
    isbn = data.get('isbn')
    langue = data.get('langue')
    prix = data.get('prix')
    date_parution = data.get('date_parution')
    categorie = data.get('categorie')
    date_disponibilite_libraire = data.get('date_disponibilite_libraire')
    date_disponibilite_particulier = data.get('date_disponibilite_particulier')
    image = data.get('image')
    table_des_matieres = data.get('table_des_matieres')
    mot_cle = data.get('mot_cle')
    description = data.get('description')

    #si les attributs sont bien récupérés
    if titre and auteur and isbn and langue and prix and date_parution and categorie and date_disponibilite_libraire and date_disponibilite_particulier and table_des_matieres and mot_cle and description :
        # remplissage avec les infos
        ouvrage = serviceOuvrage.createOuvrage(titre, 
                                      auteur,
                                      isbn,
                                      langue,
                                      prix,
                                      date_parution,
                                      categorie,
                                      date_disponibilite_libraire,
                                      date_disponibilite_particulier,
                                      image,
                                      table_des_matieres,
                                      mot_cle,
                                      description
                                      )
        return jsonify(ouvrage.serialize()), 200
    else:
        return jsonify({'message': 'Invalid input'}), 400


''' PUT
Update d'un ouvrage par son ID
'''
# @ouvrage.route('/ouvrage/<int:id_ouvrage>', methods=['PUT'])
# def updateOuvrage(id_ouvrage):
#     récupération des données
#     data = request.json

#     récupération des attributs
#     titre = data.get('titre')
#     auteur = data.get('auteur')
#     isbn = data.get('isbn')
#     langue = data.get('langue')
#     prix = data.get('prix')
#     date_parution = data.get('date_parution')
#     categorie = data.get('categorie')
#     date_disponibilite_libraire = data.get('date_disponibilite_libraire')
#     date_disponibilite_particulier = data.get('date_disponibilite_particulier')
#     image = data.get('image')
#     table_des_matieres = data.get('table_des_matieres')
#     mot_cle = data.get('mot_cle')
#     description = data.get('description')

#     if titre and auteur and isbn and langue and prix and date_parution and categorie and date_disponibilite_libraire and date_disponibilite_particulier and table_des_matieres and mot_cle and description :
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