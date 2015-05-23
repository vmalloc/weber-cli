from flask import Blueprint

blueprint = Blueprint('{{blueprint.name}}', __name__, url_prefix='{{blueprint.path}}')

@blueprint.route('/')
def index():
    return 'This is the {{blueprint.name}} blueprint'
