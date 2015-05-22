import click

from ..templates import extract_structure

@click.command()
@click.argument('directory', default='.')
@click.option('--app-name', prompt=True)
def init(directory, app_name):
    extract_structure('minimal', into=directory, ctx={
        'app': {
            'name': app_name,
        }
    })
    return 0
