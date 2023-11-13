import db

connection = db.db

class ThemeOuvrage(connection.Model):
    id_ouvrage = connection.Column(connection.Integer, primary_key=True)
    id_theme = connection.Column(connection.Integer, primary_key=True)

    def __init__(self, id_ouvrage, id_theme):
        self.id_ouvrage = id_ouvrage
        self.id_theme = id_theme

    def serialize(self):
        return {
            'id_ouvrage': self.id_ouvrage,
            'id_theme': self.id_theme,
        }
