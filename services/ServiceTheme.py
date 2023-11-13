from entites.Theme import Theme  
import db

connection = db.db

class ServiceTheme:
    def getAllThemes():
        return Theme.query.all()
    

    ''' GET
    Récupérer un thème par son ID
    '''
    def getThemeById(id_theme):
        theme = Theme.query.get(id_theme)
        return theme


    ''' POST
    Créer un nouveau thème dans la BDD
    '''
    def createTheme(nom):
        # on se sert d'un objet thème pour y remplir les informations
        new_theme = Theme(nom_theme = nom)
        # ouvrir la connexion et ajouter un thème à la BDD
        connection.session.add(new_theme)
        # sauvegarder et fermer la connexion avec la BDD
        connection.session.commit()
        return new_theme
    
    def updateTheme(theme_id, new_nom): 
        theme = Theme.query.get(theme_id)
        if theme:
            theme.nom_theme = new_nom
            connection.session.commit()
            return theme
        return None
    
    def deleteTheme(theme_id):
        theme = Theme.query.get(theme_id)
        if theme:
            connection.session.delete(theme)
            connection.session.commit()
            return True
        return False