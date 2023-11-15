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
    # récupérer tous
    ouvrages = serviceOuvrage.getAllOuvrages()
    # transformer le résultat en liste JSON
    serialized_ouvrages = [ouvrage.serializeFull() for ouvrage in ouvrages] #serializeFull pour récupérer aussi l'ID
    return jsonify(serialized_ouvrages), 200


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

    #si les attributs obligatoires sont bien récupérés
    if titre and auteur and isbn :
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
@ouvrage.route('/ouvrage/<int:id_ouvrage>', methods=['PUT'])
def updateOuvrage(id_ouvrage):
    # récupération des données
    data = request.json

    # récupération des attributs
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

    #si les attributs obligatoires sont bien récupérés
    if titre and auteur and isbn :
        updated_ouvrage = serviceOuvrage.updateOuvrage(id_ouvrage,
                      titre,
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
                      description)
        if updated_ouvrage:
            return jsonify(updated_ouvrage.serialize()), 200 
        else:
            return jsonify({'message': 'Ouvrage not found'}), 404
    else:
        return jsonify({'message': 'Invalid input'}), 400
    

''' DELETE
Supprimer un ouvrage par son ID
'''    
@ouvrage.route('/ouvrage/<int:id_ouvrage>', methods=['DELETE'])
def deleteOuvrage(id_ouvrage):
    success = serviceOuvrage.deleteOuvrage(id_ouvrage)
    if success:
        return jsonify({'message': 'Ouvrage deleted successfully'}), 200 
    else:
        return jsonify({'message': 'Ouvrage not found'}), 404