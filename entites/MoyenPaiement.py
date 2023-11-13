import db

connection = db.db

class MoyenPaiement(connection.Model):
    id_moyen_paiement = connection.Column(connection.Integer, primary_key=True, autoincrement=True)
    type_paiement = connection.Column(connection.Sting(20))
    nom_proprietaire_paiement = connection.Column(connection.String(255))
    numero_moyen_paiement = connection.Column(connection.String(255))
    date_expiration_paiement =  connection.Column(connection.DateTime)
    code_secu_paiement =  connection.Column(connection.String(4))


    def __init__(self ,type_paiement, nom_proprietaire_paiement, numero_moyen_paiement, date_expiration_paiement, code_secu_paiement):
        self.type_paiement = type_paiement
        self.nom_proprietaire_paiement = nom_proprietaire_paiement
        self.numero_moyen_paiement = numero_moyen_paiement
        self.date_expiration_paiement = date_expiration_paiement
        self.code_secu_paiement = code_secu_paiement

        
    def serialize(self):
        return {
            'type_paiement': self.type_paiement,
            'nom_proprietaire_paiement': self.nom_proprietaire_paiement,
            'numero_moyen_paiement': self.numero_moyen_paiement,
            'date_expiration_paiement': self.date_expiration_paiement,
            'code_secu_paiement': self.code_secu_paiement,
        }