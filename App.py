from flask import Flask
import db
from Conf import confDB

connection = db.db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{confDB.user}:{confDB.password}@{confDB.host}/{confDB.database}"

# Initialise la connection à la BDD
connection.init_app(app)

# Register the Controller
from controllers.ControllerClient import client
app.register_blueprint(client)

from controllers.ControllerCommande import commande
app.register_blueprint(commande)

if __name__ == '__main__':
    app.run(debug=True)