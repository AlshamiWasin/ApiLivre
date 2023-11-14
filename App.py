from flask import Flask
import db
from Conf import confDB

connection = db.db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{confDB.user}:{confDB.password}@{confDB.host}/{confDB.database}"

# Initialise la connection à la BDD
connection.init_app(app)

# Register the Controllers
#Controller Client
from controllers.ControllerClient import client
app.register_blueprint(client)

# Controller Ouvrage
from controllers.ControllerOuvrage import ouvrage
app.register_blueprint(ouvrage)

from controllers.ControllerCommande import commande
app.register_blueprint(commande)

from controllers.ControllerMoyenPaiement import moyenpaiement
app.register_blueprint(moyenpaiement)

from controllers.ControllerTheme import theme
app.register_blueprint(theme)

if __name__ == '__main__':
    app.run(debug=True)