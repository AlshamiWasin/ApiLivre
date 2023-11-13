from flask import Blueprint , request , jsonify
from services.ServiceTheme import ServiceTheme

# Create the auth app
theme = Blueprint('theme', __name__)
serviceTheme = ServiceTheme


# Define the routes
@theme.route('/themes' , methods=['GET'])
def getThemes():
    return serviceTheme.getAllThemes()
    

# Define the Routes
@theme.route('/theme/<int:id_theme>' , methods=['GET'])
def getThemeById(id_theme):
    theme = serviceTheme.getThemeById(id_theme)
    if theme:
        return jsonify(theme.serialize()), 200 
    else:
        return jsonify({'message': 'theme not found'}), 400


''' POST
Créer un nouveau thème dans la BDD
'''
@theme.route('/theme' , methods=['POST'])
def createTheme():
    data = request.json

    nom = data.get('nom')

    if nom :
        theme = serviceTheme.createtheme(data.get('nom'))

        # return jsonify(user.serialize)
        return jsonify(theme.serialize()), 200 
    else:
        return jsonify({'message': 'Invalid input'}), 400

@theme.route('/theme/<int:theme_id>', methods=['PUT'])
def updateTheme(theme_id):
    data = request.json
    new_nom = data.get('nom')

    if new_nom :
        updated_theme = serviceTheme.updatetheme(theme_id, new_nom)
        if updated_theme :
            return jsonify(updated_theme.serialize()), 200 
        else:
            return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'message': 'Invalid input'}), 400
    

@theme.route('/theme/<int:theme_id>', methods=['DELETE'])
def deleteTheme(theme_id):
    success = serviceTheme.deletetheme(theme_id)
    if success:
        return jsonify({'message': 'theme deleted successfully'}), 200 
    else:
        return jsonify({'message': 'theme not found'}), 404