# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_549 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "9GU|IJkY#:"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"\x13\xe9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x14\xe0\xd9\xd0B\xf4\xebs\xd2`]\xf1O\t\xd8W\x1b$+"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 15
    module_1.object(**var_0)
