# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1299 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "06o^"
    var_0 = module_0.func(*str_0)
    assert var_0 == 7


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "86zoy"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "79"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    module_0.func()
