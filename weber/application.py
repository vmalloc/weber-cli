import py
from flask import Flask

import yaml
import logbook
from emport import import_file


_logger = logbook.Logger(__name__)

class WeberApplication(object):

    def __init__(self, workdir):
        super(WeberApplication, self).__init__()
        self.workdir = py.path.local(workdir)
        self.flask_config = {}

    def get_blueprint_directory(self):
        return self.workdir.join('blueprints')

    def create_flask_app(self):
        returned = Flask('weber')
        returned.config.update(self.flask_config)
        self._register_blueprints(returned)
        return returned

    def _register_blueprints(self, flask_app):
        config = self._load_config()
        for blueprint_filename in self.workdir.join('blueprints').listdir():
            if blueprint_filename.ext != '.py' or blueprint_filename.basename.startswith('_'):
                _logger.debug('Ignoring {}', blueprint_filename)
                continue

            _logger.debug('Registering blueprint {.basename}', blueprint_filename)
            mod = import_file(str(blueprint_filename))
            flask_app.register_blueprint(mod.blueprint)


    def _load_config(self):
        with self._open_config_file() as f:
            return yaml.load(f)

    def _save_config(self, cfg):
        with self._open_config_file('w') as f:
            yaml.dump(cfg, f, encoding='utf-8')

    def _open_config_file(self, *args):
        return self.workdir.join('weber_config.yml').open(*args)
