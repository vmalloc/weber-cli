# put py.test fixtures here
import pytest


@pytest.fixture
def text1():
    return """This is a
    multiline
    text\t\t/# with
    Some ' Special
    " characters
    """
