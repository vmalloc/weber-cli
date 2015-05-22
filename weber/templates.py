import os

import logbook
from jinja2 import Environment, PackageLoader

_logger = logbook.Logger(__name__)


def extract_template(name, into, ctx=None):
    template = _get_template(name)
    filename = os.path.basename(name)

    if not os.path.isdir(into):
        _logger.debug('Creating directory {}', into)
        os.makedirs(into)

    with open(os.path.join(into, filename), 'w') as f:
        f.write(template.render(ctx))

def extract_structure(name, into, ctx=None):
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '_templates'))
    _logger.debug('Walking {}', template_dir)
    for path, _, filenames in os.walk(template_dir):
        for filename in filenames:
            template_name = os.path.relpath(os.path.join(path, filename), template_dir)
            _logger.debug('Rendering {}', template_name)
            extract_template(template_name, into=into, ctx=ctx)


def _get_template(name):
    return _get_jinja_env().get_template(name)


def _get_jinja_env():
    return Environment(loader=PackageLoader('weber', '_templates'))
