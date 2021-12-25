from ..need_to_move import need_to_move
from ..is_cbs import is_cbs
import pytest
import unittest


@pytest.mark.parametrize("a, b", [('()', True),
                               ('()()(())', True),
                               (')(', False),
                               ('()(', False),
                               ('(()', False),
                               ('(((', False)
                               ])
def test_is_cbs(a, b):
    assert is_cbs(a) == b


def test_need_to_move():
    assert need_to_move('())(') == 1
    assert not need_to_move('((())(')
    assert need_to_move('()()))((') == 2
    assert not need_to_move('(((')
    assert need_to_move(')))(((') == 3


@pytest.mark.parametrize("a, b", [('()()))((', 2),
                                  ('()))((', 2)])
def test_example(a, b):
    assert need_to_move(a) == b


@pytest.fixture()
def param():
    return '())('


def test_for_fixture(param):
    assert not is_cbs(param)
    assert need_to_move(param) == 1


class NeedToMoveTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(need_to_move('())('), 1)


if __name__ == '__main__':
    unittest.main()
