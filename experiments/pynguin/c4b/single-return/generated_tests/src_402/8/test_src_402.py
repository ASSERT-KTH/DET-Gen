# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_402 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2237
    list_0 = [int_0, int_0, int_0, int_0]
    list_1 = [int_0, list_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2237
    list_0 = []
    list_1 = [int_0, list_0, int_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "7"
    bool_0 = True
    list_0 = [bool_0, str_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    str_0 = "4Z"
    bool_1 = True
    list_0 = [bool_0, str_0, str_0, bool_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    list_1 = []
    list_2 = [bool_1, list_1]
    var_1 = module_0.func(*list_2)
    assert var_1 == "YES"
    module_0.func()
