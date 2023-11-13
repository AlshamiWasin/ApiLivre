from entites.Client import Client  
import db

connection = db.db

class ServiceClient:
    def getAllClients():
        return Client.query.all()
    


    def getClientById(id_client):
        client = Client.query.get(id_client)
        return client

    def createClient(nom , prenom , email ,tel ):
        new_client = Client(nom_client = nom, 
                            prenom_client = prenom, 
                            email_client = email , 
                            telephone_client = tel )
        # ouvrir la connection avec las BD et ajouter un client a la BD
        connection.session.add(new_client)
        # fermer la connection avec las BD
        connection.session.commit()
        return new_client
    
