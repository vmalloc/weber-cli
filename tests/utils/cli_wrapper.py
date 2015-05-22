import os
import subprocess
import sys

from click.testing import CliRunner as ClickRunner
from weber.cli.weber import main


class CLIWrapper(object):

    def __init__(self):
        super(CLIWrapper, self).__init__()
        self._running = []

    def run(self, argv, assert_success=True, cwd=None):
        try:
            main.main(args=[str(x) for x in argv])
        except SystemExit as e:
            return e.code
        else:
            assert False, 'Not finished'

    def start_process(self, args, cwd):
        p = subprocess.Popen([os.path.join(os.path.dirname(sys.executable), 'weber')] + map(str, args), cwd=str(cwd))
        self._running.append(p)
        return p

    def terminate_all(self):
        for p in self._running:
            p.terminate()
