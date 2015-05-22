import click

@click.group()
def main():
    pass

from .init import init
main.add_command(init)

from .testserver import testserver
main.add_command(testserver)


if __name__ == "__main__":
    main(prog_name='weber')
