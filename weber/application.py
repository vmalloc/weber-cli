from flask import Flask


class Application(object):

    def __init__(self):
        super(Application, self).__init__()
        self.flask_config = {}

    def create_flask_app(self):
        returned = Flask('weber')
        returned.config.update(self.flask_config)
        return returned
