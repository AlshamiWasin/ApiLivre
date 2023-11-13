import db

connection = db.db

class Commantaire(connection.Model):
    id_commantaire = connection.Column(connection.Integer, primary_key=True, autoincrement=True)
    id_client = connection.Column(connection.Integer, index=True)
    id_ouvrage = connection.Column(connection.Integer, index=True)
    date_publication_commentaire = connection.Column(connection.DateTime)
    auteur_commentaire =  connection.Column(connection.String(255))
    titre_commentaire =  connection.Column(connection.String(255))


    def __init__(self , id_client, id_ouvrage, date_publication_commentaire, auteur_commentaire, titre_commentaire):
        self.id_client = id_client
        self.id_ouvrage = id_ouvrage
        self.date_publication_commentaire = date_publication_commentaire
        self.auteur_commentaire = auteur_commentaire
        self.titre_commentaire = titre_commentaire


    def serialize(self):
        return {
            'id_client': self.id_client,
            'id_ouvrage': self.id_ouvrage,
            'date_publication_commentaire': self.date_publication_commentaire,
            'auteur_commentaire': self.auteur_commentaire,
            'titre_commentaire': self.titre_commentaire,
        }