import db

connection = db.db

class Commande(connection.Model):
    id_commande = connection.Column(connection.Integer, primary_key=True, autoincrement=True)
    id_client = connection.Column(connection.Integer, index=True)
    id_ouvrage = connection.Column(connection.Integer, index=True)
    id_moyen_paiement = connection.Column(connection.Integer, index=True)
    date_commande =  connection.Column(connection.DateTime)
    montant =  connection.Column(connection.Float)


    def __init__(self , id_client, id_ouvrage, id_moyen_paiement, date_commande, montant):
        self.id_client = id_client
        self.id_ouvrage = id_ouvrage
        self.id_moyen_paiement = id_moyen_paiement
        self.date_commande = date_commande
        self.montant = montant

        
    def serialize(self):
        return {
            'id_client': self.id_client,
            'id_ouvrage': self.id_ouvrage,
            'id_moyen_paiement': self.id_moyen_paiement,
            'date_commande': self.date_commande,
            'montant': self.montant,
        }