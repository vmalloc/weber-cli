# put py.test fixtures here
import pytest
import py
import os

from .utils.cli_wrapper import CLIWrapper
from .utils.deployment import deploy_testserver, Deployment


def pytest_addoption(parser):
    parser.addoption("--deployment-type", action="store", default="testserver",
                     help="testserver/local/vagrant/remote:[user@host]")


@pytest.fixture(scope='session')
def deployment(request, full_app_dir):
    dtype = os.environ.get('WEBER_UT_DEPLOYMENT_TYPE')
    if dtype is None:
        dtype = request.config.getoption('--deployment-type')
    if dtype == 'testserver':
        deploy_testserver(request, full_app_dir)
        return Deployment('http://127.0.0.1:8000')
    else:
        raise NotImplementedError()  # pragma: no cover

@pytest.fixture(scope='session')
def full_app_dir(request):
    directory = py.path.local.mkdtemp()
    request.addfinalizer(directory.remove)

    directory = directory.join('project')

    cli = CLIWrapper()
    cli.run(['init', directory, '--app-name', 'sample'])
    cli.run(['-w', directory, 'generate', 'blueprint', 'index', '--path=/'])

    return directory




@pytest.fixture
def cli(request):
    returned = CLIWrapper()
    return returned


@pytest.fixture
def init_dir(tmpdir, app_name, cli):
    returned = tmpdir.join('project')
    cli.run(['init', returned, '--app-name', app_name])
    return returned


@pytest.fixture
def app_name():
    return 'some_app_name'
