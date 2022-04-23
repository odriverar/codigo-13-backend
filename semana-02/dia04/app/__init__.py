from flask import Flask

## Importamos blueprint

from .admin import admin
from .portafolio import portafolio

#importamos el config
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(admin)
    app.register_blueprint(portafolio)
    
    return app