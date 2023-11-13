import db

# Liaison avec la BDD
connection = db.db

class Client(connection.Model):
    id_client = connection.Column(connection.Integer, primary_key=True, autoincrement=True)
    nom_client = connection.Column(connection.String(255))
    prenom_client = connection.Column(connection.String(255))
    email_client = connection.Column(connection.String(255))
    telephone_client = connection.Column(connection.String(20))
    preferences_client = connection.Column(connection.Text)
    adresse_livraison_client = connection.Column(connection.Text)
    adresse_facturation_client = connection.Column(connection.Text)

    def __init__(self , nom_client, prenom_client, email_client , telephone_client):
        self.nom_client = nom_client
        self.prenom_client = prenom_client
        self.email_client = email_client
        self.telephone_client = telephone_client


    # def serialize(self):
    #     return {
    #         'id_client': self.id_client,
    #         'nom_client': self.nom_client,
    #         'prenom_client': self.prenom_client,
    #         'email_client': self.email_client,
    #         'telephone_client': self.telephone_client,
    #         'preferences_client': self.preferences_client,
    #         'adresse_livraison_client': self.adresse_livraison_client,
    #         'adresse_facturation_client': self.adresse_facturation_client
    #     }

    def serialize(self):
        return {
            'nom_client': self.nom_client,
            'prenom_client': self.prenom_client,
            'email_client': self.email_client,
            'telephone_client': self.telephone_client,
        }