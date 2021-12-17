from ..need_to_move import need_to_move
from ..is_cbs import is_cbs
import pytest


def test_need_to_move():
    assert is_cbs('()')
    assert is_cbs('()()(())')
    assert not is_cbs(')(')
    assert not is_cbs('()(')
    assert not is_cbs('(()')
    assert not is_cbs('(((')


def test_need_to_move():
    assert need_to_move('())(') == 1
    assert not need_to_move('((())(')
    assert need_to_move('()()))((') == 2
    assert not need_to_move('(((')
    assert need_to_move(')))(((') == 3


@pytest.mark.parametrize("a", ['()',
                               '()('])
def example(a):
    assert is_cbs('a')
    assert not is_cbs('a')


@pytest.fixture()
def param():
    return '())('


def test_for_fixture(param):
    is_cbs(param)
    assert need_to_move(param) == 1
