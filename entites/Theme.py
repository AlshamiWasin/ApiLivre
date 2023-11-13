import db

connection = db.db

class Theme(connection.Model):
    id_theme  = connection.Column(connection.Integer, primary_key=True, autoincrement=True)
    nom_theme = connection.Column(connection.String(255))

    def __init__(self , nom_theme):
        self.nom_theme = nom_theme


    def serialize(self):
        return {
            'nom_theme': self.nom_theme,
        }