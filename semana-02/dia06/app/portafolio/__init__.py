from flask import Blueprint

portafolio = Blueprint('portafolio',__name__,url_prefix='/')
# proyectos = Blueprint('proyectos', __name__,url_prefix='/proyectos')
# acercade = Blueprint('abaut', __name__, url_prefix='/about')
# contacto = Blueprint('contacto', __name__, url_prefix='/')

from . import views