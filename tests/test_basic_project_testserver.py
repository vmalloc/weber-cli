import requests


def test_basic_project_run(init_dir, cli, testserver):
    p = cli.start_process(cwd=init_dir, args=['testserver'])
    assert testserver.get('/', assert_success=False).status_code == requests.codes.not_found
