import click


@click.command()
@click.option('-p', '--port', type=int, default=8000)
@click.pass_context
def testserver(ctx, port):
    app = ctx.obj
    app.flask_config.update(DEBUG=True, TESTING=True)
    app.create_flask_app().run(port=port)
