from entites.Client import Client  
import db

connection = db.db

class ServiceClient:
    def getAllClients():
        return Client.query.all()
    

    ''' GET
    Récupérer un client par son ID
    '''
    def getClientById(id_client):
        client = Client.query.get(id_client)
        return client


    ''' POST
    Créer un nouveau client dans la BDD
    '''
    def createClient(nom, prenom, email, tel ):
        # on se sert d'un objet client pour y remplir les informations
        new_client = Client(nom_client = nom, 
                            prenom_client = prenom, 
                            email_client = email , 
                            telephone_client = tel )
        # ouvrir la connexion et ajouter un client à la BDD
        connection.session.add(new_client)
        # sauvegarder et fermer la connexion avec la BDD
        connection.session.commit()
        return new_client
    
