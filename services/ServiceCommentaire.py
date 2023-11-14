from entites.Commentaire import Commentaire  
import db

connection = db.db

class ServiceCommentaire:

    ''' GET
    Récupérer tous les commentaires
    ''' 
    def getAllCommentaires():
        return Commentaire.query.all()
    

    ''' GET
    Récupérer un commentaire par son ID
    '''
    def getCommentaireById(id_commentaire):
        commentaire = Commentaire.query.get(id_commentaire)
        return commentaire


    ''' POST
    Créer un nouveau commentaire dans la BDD
    '''
    def createCommentaire(date, auteur, titre):
        # on se sert d'un objet commentaire pour y remplir les informations
        new_commentaire = Commentaire(date_publication_commentaire = date, 
                            auteur_commentaire = auteur, 
                            titre_commentaire = titre)
        # ouvrir la connexion et ajouter un commentaire à la BDD
        connection.session.add(new_commentaire)
        # sauvegarder et fermer la connexion avec la BDD
        connection.session.commit()
        return new_commentaire
    
    def updateCommentaire(commentaire_id, new_date, new_auteur, new_titre): 
        commentaire = Commentaire.query.get(commentaire_id)
        if commentaire:
            commentaire.date_publication_commentaire = new_date
            commentaire.auteur_commentaire = new_auteur
            commentaire.titre_commentaire = new_titre
            connection.session.commit()
            return commentaire
        return None
    
    def deleteCommentaire(commentaire_id):
        commentaire = Commentaire.query.get(commentaire_id)
        if commentaire:
            connection.session.delete(commentaire)
            connection.session.commit()
            return True
        return False