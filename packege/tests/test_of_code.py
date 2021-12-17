from ..need_to_move import need_to_move
from ..is_cbs import is_cbs
import pytest


def test_is_cbs():
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


@pytest.mark.parametrize("a", ['()()))((',
                               '()))(('])
def test_example(a):
    assert need_to_move(a) == 2
    assert need_to_move(a) == 2


@pytest.fixture()
def param():
    return '())('


def test_for_fixture(param):
    assert not is_cbs(param)
    assert need_to_move(param) == 1
