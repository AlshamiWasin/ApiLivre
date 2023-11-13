import db

connection = db.db

class ClientMoyenPaiement(connection.Model):
    id_client = connection.Column(connection.Integer, primary_key=True)
    id_moyen_paiement  = connection.Column(connection.Integer, primary_key=True)

    def __init__(self, id_client, id_moyen_paiement):
        self.id_client = id_client
        self.id_moyen_paiement  = id_moyen_paiement

    def serialize(self):
        return {
            'id_client': self.id_client,
            'id_moyen_paiement': self.id_moyen_paiement,
        }
