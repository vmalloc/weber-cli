import os
import subprocess
import sys
import time

import requests


def deploy_testserver(request, full_app_dir):
    p = subprocess.Popen(
        [
            os.path.join(os.path.dirname(sys.executable), 'weber'),
            'testserver'],
        cwd = full_app_dir.strpath)
    request.addfinalizer(p.terminate)
    _wait_until_connected()


class Deployment(object):

    def __init__(self, url):
        super(Deployment, self).__init__()
        self.url = url

    def get(self, path):
        returned = requests.get(self.url + path)
        returned.raise_for_status()
        return returned

def _wait_until_connected(retries=10, sleep=0.1):
    for retry in range(retries):
        if retry > 0:
            time.sleep(sleep)
        try:
            requests.get('http://127.0.0.1:8000')
            return
        except requests.ConnectionError:
            pass
    raise RuntimeError('Could not connect')
