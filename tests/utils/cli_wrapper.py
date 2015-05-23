import os
import sys

from click.testing import CliRunner as ClickRunner
from weber.cli.weber import main


class CLIWrapper(object):

    def __init__(self):
        super(CLIWrapper, self).__init__()
        self._running = []

    def run(self, argv, assert_success=True, cwd=None):
        args = [str(x) for x in argv]
        if cwd is not None:
            args = ['-w', cwd] + args
        try:
            main.main(args=args)
        except SystemExit as e:
            assert e.code == 0
        else:
            assert False, 'Not finished'

