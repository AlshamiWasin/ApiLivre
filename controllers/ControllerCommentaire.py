from flask import Blueprint , request , jsonify
from services.ServiceCommentaire import ServiceCommentaire

# Create the auth app
commentaire = Blueprint('commentaire', __name__)
serviceCommentaire = ServiceCommentaire


# Define the routes
@commentaire.route('/commentaires' , methods=['GET'])
def getCommentaires():
    commentaires = serviceCommentaire.getAllCommentaires()
    serialized_commentaires = [commentaire.serialize() for commentaire in commentaires]
    return jsonify(serialized_commentaires)
    

# Define the Routes
@commentaire.route('/commentaire/<int:id_commentaire>' , methods=['GET'])
def getCommentaireById(id_commentaire):
    commentaire = serviceCommentaire.getCommentaireById(id_commentaire)
    if commentaire:
        return jsonify(commentaire.serialize()), 200 
    else:
        return jsonify({'message': 'Commentaire not found'}), 400


''' POST
Créer un nouveau commentaire dans la BDD
'''
@commentaire.route('/commentaire' , methods=['POST'])
def createCommentaire():
    data = request.json

    date = data.get('date_publication_commentaire')
    auteur = data.get('auteur_commentaire')
    titre = data.get('titre_commentaire')

    if date and auteur and titre:
        commentaire = serviceCommentaire.createCommentaire(date,
                                      auteur,
                                      titre)
        # return jsonify(user.serialize)
        return jsonify(commentaire.serialize()), 200 
    else:
        return jsonify({'message': 'Invalid input'}), 400

@commentaire.route('/commentaire/<int:commentaire_id>', methods=['PUT'])
def updateCommentaire(commentaire_id):
    data = request.json
    new_date= data.get('date')
    new_auteur = data.get('auteur')
    new_titre = data.get('titre')

    if new_date and new_auteur and new_titre:
        updated_commentaire = serviceCommentaire.updateCommentaire(commentaire_id, new_date, new_auteur , new_titre)
        if updated_commentaire:
            return jsonify(updated_commentaire.serialize()), 200 
        else:
            return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'message': 'Invalid input'}), 400
    

@commentaire.route('/commentaire/<int:commentaire_id>', methods=['DELETE'])
def deleteCommentaire(commentaire_id):
    success = serviceCommentaire.deleteCommentaire(commentaire_id)
    if success:
        return jsonify({'message': 'Commentaire deleted successfully'}), 200 
    else:
        return jsonify({'message': 'Commentaire not found'}), 404