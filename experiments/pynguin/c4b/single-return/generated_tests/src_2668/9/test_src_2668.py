# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2668 as module_0


def test_case_0():
    str_0 = "1talu,"
    var_0 = module_0.func(*str_0)
    assert var_0 == "0"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "10w\t-qJlu"
    int_0 = 220
    list_0 = [int_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1talu,"
    bool_0 = True
    list_0 = [bool_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    var_1 = module_0.func(*str_0)
    assert var_1 == "0"
    module_0.func(*var_1)


def test_case_4():
    str_0 = "10Gtalu"
    var_0 = module_0.func(*str_0)
    assert var_0 == "00"