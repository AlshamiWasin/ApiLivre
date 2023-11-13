from entites.Ouvrage import Ouvrage  
import db

connection = db.db

class ServiceOuvrage:

    ''' GET
    Récupérer tous les ouvrages
    '''    
    def getAllOuvrages():
        return Ouvrage.query.all()
    

    ''' GET
    Récupérer un ouvrage par son ID
    '''
    def getOuvrageById(id_ouvrage):
        ouvrage = Ouvrage.query.get(id_ouvrage)
        return ouvrage


    ''' POST
    Créer un nouvel ouvrage dans la BDD
    Avec en paramètres seulement titre et auteur
    Utile pour tester rapidement !
    '''
    def createOuvrageTitreAuteur(titre, auteur):
        # on se sert d'un objet Ouvrage pour y remplir les informations
        new_ouvrage = Ouvrage(titre_ouvrage = titre, 
                            auteur_ouvrage = auteur)
        # ouvrir la connexion et ajouter un client à la BDD
        connection.session.add(new_ouvrage)
        # sauvegarder et fermer la connexion avec la BDD
        connection.session.commit()
        return new_ouvrage
    

    ''' POST
    Créer un nouvel ouvrage dans la BDD
    Avec tous les paramètres
    '''
    def createOuvrageTitreAuteur(titre, auteur):
        # on se sert d'un objet Ouvrage pour y remplir les informations
        new_ouvrage = Ouvrage(titre_ouvrage = titre, 
                            auteur_ouvrage = auteur)
        # ouvrir la connexion et ajouter un client à la BDD
        connection.session.add(new_ouvrage)
        # sauvegarder et fermer la connexion avec la BDD
        connection.session.commit()
        return new_ouvrage
    
    # def updateClient(client_id, new_nom, new_prenom , new_email, new_tel): 
    #     client = Client.query.get(client_id)
    #     if client:
    #         client.nom_client = new_nom
    #         client.prenom_client = new_prenom
    #         client.email_client = new_email
    #         client.telephone_client = new_tel
    #         connection.session.commit()
    #         return client
    #     return None
    
    # def deleteClient(client_id):
    #     client = Client.query.get(client_id)
    #     if client:
    #         connection.session.delete(client)
    #         connection.session.commit()
    #         return True
    #     return False