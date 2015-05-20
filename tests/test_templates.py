from weber.utils.template import TemplateSet


def test_single_file(tmpdir, text1):
    filename = tmpdir.join('filename')
    TemplateSet.from_string(text1).extract(filename)
    with filename.open() as f:
        assert f.read() == text1
