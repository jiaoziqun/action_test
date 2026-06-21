# pytest文件
import pytest
from git_action_test import calculate


def test_add():
    calc = calculate(10, 5)
    assert calc.Add() == 15


def test_sub():
    calc = calculate(10, 5)
    assert calc.Sub() == 5


def test_mul():
    calc = calculate(10, 5)
    assert calc.Mul() == 50


def test_div():
    calc = calculate(10, 5)
    assert calc.Div() == 2.0


def test_power():
    calc = calculate(10, 5)
    assert calc.power() == 100000


def test_power_by_zero():
    calc = calculate(10, 0)
    assert calc.power() == 1


def test_div_by_zero():
    calc = calculate(10, 0)
    with pytest.raises(ZeroDivisionError):
        calc.Div()
