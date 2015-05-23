import click

from ..application import WeberApplication

@click.group()
@click.option('-w', '--workdir', default='.')
@click.pass_context
def main(ctx, workdir):
    ctx.obj = WeberApplication(workdir)

from .init import init
main.add_command(init)

from .testserver import testserver
main.add_command(testserver)

from .generate import generate
main.add_command(generate)



if __name__ == "__main__":
    main(prog_name='weber')
