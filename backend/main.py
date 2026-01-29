from flask import Flask
from flask_restx import Api
from config import DevConfig
from flask_jwt_extended import JWTManager
from exts import db
from flask_migrate import Migrate
from models import Recipe, User
from auth import auth_ns
from recipes import recipe_ns
from flask_cors import CORS


# create a factory function
def create_app(config):
    # initialise the app
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app)

    db.init_app(app)

    # instantiate migrate class
    migrate = Migrate(app, db)
    # instantiate jwt
    JWTManager(app)

    api = Api(app, doc = '/docs') 

    api.add_namespace(auth_ns)
    api.add_namespace(recipe_ns)

    # model(serializer)
    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "Recipe": Recipe,
            "User": User
        }
    
    return app




