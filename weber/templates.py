import os

import logbook
from jinja2 import Environment, PackageLoader

_logger = logbook.Logger(__name__)


def extract_template(name, dest, ctx=None):
    dest = str(dest)
    if ctx is None:
        ctx = {}

    template = _get_template(name)
    dirname = os.path.dirname(dest)
    if not os.path.isdir(dirname):
        _logger.debug('Creating directory {}', dirname)
        os.makedirs(dirname)

    with open(dest, 'w') as f:
        f.write(template.render(ctx))

def extract_structure(name, into, ctx=None):
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '_templates'))
    structure = os.path.join(template_dir, name)
    _logger.debug('Walking {}', template_dir)
    for path, _, filenames in os.walk(structure):
        for filename in filenames:
            filename = os.path.join(path, filename)
            template_name = os.path.relpath(filename, template_dir)

            dest = os.path.join(into, os.path.relpath(filename, structure))

            _logger.debug('Rendering {} --> {}', template_name, dest)

            extract_template(template_name, dest, ctx=ctx)


def _get_template(name):
    return _get_jinja_env().get_template(name)


def _get_jinja_env():
    return Environment(loader=PackageLoader('weber', '_templates'))
