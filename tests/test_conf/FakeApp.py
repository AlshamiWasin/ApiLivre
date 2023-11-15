from services.ServiceClient import ServiceClient
from flask import Flask

from Conf import confDB
import db
connection = db.db


def create_app():
    app = Flask(__name__)

    # Configure the app (database connection, secret key, etc.)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{confDB.user}:{confDB.password}@{confDB.host}/{confDB.database}"

    # Initialise la connection à la BDD
    connection.init_app(app)
    # Register blueprints (if you're using them)
    from controllers.ControllerClient import client
    app.register_blueprint(client)

    from controllers.ControllerTheme import theme
    app.register_blueprint(theme)
    
    from controllers.ControllerOuvrage import ouvrage
    app.register_blueprint(ouvrage)

    return app