# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1132 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "~IV`?Dj'}"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


def test_case_2():
    str_0 = "BBBBBBBB3h!G+RK\t*0"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8
