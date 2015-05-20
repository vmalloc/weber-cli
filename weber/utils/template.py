import jinja2
from .._compat import cStringIO

class TemplateSet(object):

    def __init__(self):
        super(TemplateSet, self).__init__()
        self._templates = {}

    @classmethod
    def from_string(cls, s):
        return cls.from_file(cStringIO(s))

    @classmethod
    def from_file(cls, f):
        self = cls()
        self._templates[None] = jinja2.Template(f.read())
        return self

    def extract(self, path):
        assert len(self._templates) == 1
        assert self._templates.keys()[0] is None
        with open(str(path), 'w') as f:
            f.write(self._templates[None].render())

