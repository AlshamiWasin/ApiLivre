from entites.Commande import Commande
import db

connection = db.db

class ServiceCommande:

    ''' GET
    Récupérer tous les commandes
    '''
    def getAllCommande():
        return Commande.query.all()