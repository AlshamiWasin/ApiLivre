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
    # swagger
    """
    Get : Liste des ouvrages
    ---
    
    responses:
      200:
        description: Ouvrages list.
    """
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
    # swagger
    """
    Get : Un ouvrage par son ID
    ---
    
    parameters:
      -  name: id_ouvrage
         in: path
         required: true
         schema:
           type : integer
    responses:
      200:
        description: Ouvrage found
      400:
        description: Ouvrage not found
    """
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
    # swagger
    """
    Post : Ajouter un ouvrage
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            titre:
              type: string
              description: Titre
              required: true
            auteur:
              type: string
              description: Auteur
              required: true
            isbn:
              type: string
              description: ISBN
              required: true
            langue:
              type: string
              description: Langue
            prix:
              type: number
              description: Prix
            date_parution:
              type: string
              format: date
              description: Date de parution
            categorie:
              type: string
              description: Catégorie
            date_disponibilite_libraire:
              type: string
              format: date
              description: Date de disponibilité pour les librairies
            date_disponibilite_particulier:
              type: string
              format: date
              description: Date de disponibilité pour les particuliers
            image:
              type: string
              description: URL de la couverture
            table_des_matieres:
              type: string
              description: Table des matières
            mot_cle:
              type: string
              description: Mots-clés
            description:
              type: string
              description: Description
    responses:
      200:
        description: Ouvrage ajouté avec succès
      400:
        description: Invalid input
    """
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
    # SWAGGER
    """
    Update : Modifier un ouvrage par l'ID
    ---
    parameters:
      - name: id_ouvrage
        in: path
        type: integer
        required: true
        description: L'ID de l'ouvrage à modifier
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            titre:
              type: string
              description: Titre
              required: true
            auteur:
              type: string
              description: Auteur
              required: true
            isbn:
              type: string
              description: ISBN
              required: true
            langue:
              type: string
              description: Langue
            prix:
              type: number
              description: Prix
            date_parution:
              type: string
              format: date
              description: Date de parution
            categorie:
              type: string
              description: Catégorie
            date_disponibilite_libraire:
              type: string
              format: date
              description: Date de disponibilité pour les librairies
            date_disponibilite_particulier:
              type: string
              format: date
              description: Date de disponibilité pour les particuliers
            image:
              type: string
              description: URL de la couverture
            table_des_matieres:
              type: string
              description: Table des matières
            mot_cle:
              type: string
              description: Mots-clés
            description:
              type: string
              description: Description
    responses:
      200:
        description: Ouvrage updated successfully
      404:
        description: Ouvrage not found
      400:
        description: Invalid input
    """    
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
    """
    Delete : Supprimer un ouvrage par l'ID
    ---
    parameters:
      - name: id_ouvrage
        in: path
        type: integer
        required: true
        description: L'ID de l'ouvrage à supprimer
    responses:
      200:
        description: Ouvrage deleted successfully
      404:
        description: Ouvrage not found
    """
    success = serviceOuvrage.deleteOuvrage(id_ouvrage)
    if success:
        return jsonify({'message': 'Ouvrage deleted successfully'}), 200 
    else:
        return jsonify({'message': 'Ouvrage not found'}), 404