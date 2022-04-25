from flask import Flask

from flask_bootstrap import Bootstrap

## Importamos blueprint

from .admin import admin
from .portafolio import portafolio

#importamos el config
from .config import Config

def create_app():
    app = Flask(__name__)
    
    bootstrap = Bootstrap(app)
    
    app.config.from_object(Config)
    
    app.register_blueprint(admin)
    app.register_blueprint(portafolio)
    
    return app