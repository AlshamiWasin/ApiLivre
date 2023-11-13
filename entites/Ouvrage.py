import db

connection = db.db

class Ouvrage(connection.Model):
    id_ouvrage = connection.Column(connection.Integer, primary_key=True, autoincrement=True)
    titre_ouvrage = connection.Column(connection.String(255))
    auteur_ouvrage = connection.Column(connection.String(255))
    isbn_ouvrage = connection.Column(connection.String(20))
    langue_ouvrage =  connection.Column(connection.String(20))
    prix_ouvrage =  connection.Column(connection.Float)
    date_parution_ouvrage = connection.Column(connection.DateTime)
    categorie_ouvrage = connection.Column(connection.String(255))
    date_disponibilite_libraire_ouvrage = connection.Column(connection.DateTime)
    date_disponibilite_particulier_ouvrage = connection.Column(connection.DateTime)
    image_ouvrage =  connection.Column(connection.String(255))
    table_des_matieres_ouvrage =  connection.Column(connection.String)
    mot_cle_ouvrage =  connection.Column(connection.String)
    description_ouvrage =  connection.Column(connection.String)


    def __init__(self, titre_ouvrage, auteur_ouvrage, langue_ouvrage, prix_ouvrage, date_parution_ouvrage, categorie_ouvrage, date_disponibilite_libraire_ouvrage, date_disponibilite_particulier_ouvrage, image_ouvrage, table_des_matieres_ouvrage, mot_cle_ouvrage, description_ouvrage):
        self.titre_ouvrage = titre_ouvrage
        self.auteur_ouvrage = auteur_ouvrage
        self.langue_ouvrage = langue_ouvrage
        self.prix_ouvrage = prix_ouvrage
        self.date_parution_ouvrage = date_parution_ouvrage
        self.categorie_ouvrage = categorie_ouvrage
        self.date_disponibilite_libraire_ouvrage = date_disponibilite_libraire_ouvrage
        self.date_disponibilite_particulier_ouvrage = date_disponibilite_particulier_ouvrage
        self.image_ouvrage = image_ouvrage
        self.table_des_matieres_ouvrage = table_des_matieres_ouvrage
        self.date_parution_ouvrage = date_parution_ouvrage
        self.mot_cle_ouvrage = mot_cle_ouvrage
        self.description_ouvrage = description_ouvrage

    def __init__(self, titre_ouvrage, auteur_ouvrage):
        self.titre_ouvrage = titre_ouvrage,
        self.auteur_ouvrage = auteur_ouvrage
    

    def serialize(self):
        return {
            'id_ouvrage': self.id_ouvrage,
            'titre_ouvrage': self.titre_ouvrage,
            'auteur_ouvrage': self.auteur_ouvrage,
            'langue_ouvrage': self.langue_ouvrage,
            'prix_ouvrage': self.prix_ouvrage,
            'date_parution_ouvrage': self.date_parution_ouvrage,
            'categorie_ouvrage': self.categorie_ouvrage,
            'date_disponibilite_libraire_ouvrage': self.date_disponibilite_libraire_ouvrage,
            'date_disponibilite_particulier_ouvrage': self.date_disponibilite_particulier_ouvrage,
            'image_ouvrage': self.image_ouvrage,
            'table_des_matieres_ouvrage': self.table_des_matieres_ouvrage,
            'date_parution_ouvrage': self.date_parution_ouvrage,
            'mot_cle_ouvrage': self.mot_cle_ouvrage,
            'description_ouvrage': self.description_ouvrage,
        }