# put py.test fixtures here
import pytest

from .utils.cli_wrapper import CLIWrapper
from .utils.testserver import TestServer


@pytest.fixture
def cli(request):
    returned = CLIWrapper()
    request.addfinalizer(returned.terminate_all)
    return returned


@pytest.fixture
def testserver():
    return TestServer()


@pytest.fixture
def init_dir(tmpdir, app_name, cli):
    returned = tmpdir.join('project')
    cli.run(['init', returned, '--app-name', app_name])
    return returned


@pytest.fixture
def app_name():
    return 'some_app_name'
