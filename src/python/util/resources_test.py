
from util.resources import get_lines


def test_get_lines():
    assert ['banana', 'apple', 'orange', 'pear'] == get_lines(__name__, 'resources_test.txt')
