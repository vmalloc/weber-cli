import click

from ..application import Application


@click.command()
@click.option('-p', '--port', type=int, default=8000)
def testserver(port):
    weber_app = Application()
    weber_app.flask_config.update(DEBUG=True, TESTING=True)
    flask_app = weber_app.create_flask_app().run(port=port)
