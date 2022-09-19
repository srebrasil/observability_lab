import pytest
from classes.Calc import Calc


def test_sum():
    calc = Calc(10, 5)
    assert calc.sum() == 15

def test_sub():
    calc = Calc(10, 5)
    assert calc.sub() == 5

def test_mult():
    calc = Calc(10, 5)
    assert calc.mult() == 50

def test_div():
    calc = Calc(10, 5)
    assert calc.div() == 2
