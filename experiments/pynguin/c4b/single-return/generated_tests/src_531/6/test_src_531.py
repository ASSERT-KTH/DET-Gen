# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_531 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "9\n5"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "9\n9"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 300


def test_case_3():
    str_0 = "0\r9\n9"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 10


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "0\r97\n9"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 97
    module_0.func()
