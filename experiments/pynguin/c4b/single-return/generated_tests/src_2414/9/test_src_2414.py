# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2414 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "5U\ni\\'w+"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Howard"
    module_0.func()


def test_case_2():
    str_0 = "9)3KLpl1c8J_%"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Leonard"


def test_case_3():
    str_0 = "22"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Leonard"
    var_1 = module_0.func(*list_0)
    assert var_1 == "Leonard"
