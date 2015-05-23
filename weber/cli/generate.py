import click

from .. import templates

@click.group()
def generate():
    pass

@generate.command()
@click.argument('name')
@click.option('--path', required=True)
@click.pass_context
def blueprint(ctx, name, path):
    app = ctx.obj
    templates.extract_template(
        'snippets/blueprint.py',
        app.get_blueprint_directory().join(name + '.py'),
        ctx={
            'blueprint': {'name': name, 'path': path}})
