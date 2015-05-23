import requests

def test_index_blueprint(deployment):
    assert deployment.get('/').status_code == requests.codes.ok
