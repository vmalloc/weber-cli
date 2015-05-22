import time

import requests


class TestServer(object):

    def __init__(self):
        super(TestServer, self).__init__()
        self._got_response = False

    def request(self, method, *args, **kwargs):
        assert_success = kwargs.pop('assert_success', True)
        for retry in range(5):
            if retry > 0:
                time.sleep(0.1)
            try:
                returned = requests.request(
                    method, 'http://127.0.0.1:8000/' + args[0], *args[1:], **kwargs)
            except requests.ConnectionError:
                if self._got_response:
                    raise
                continue
            self._got_response = True
            break
        else:
            assert False, 'Could not connect'
        if assert_success:
            assert returned.status_code == requsts.codes.ok
        return returned

    def get(self, *args, **kwargs):
        return self.request('GET', *args, **kwargs)

