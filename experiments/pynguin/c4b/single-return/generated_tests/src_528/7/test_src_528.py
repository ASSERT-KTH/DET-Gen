# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_528 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1709
    dict_0 = {int_0: int_0}
    list_0 = [int_0, int_0, int_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Leonard"
    list_1 = [int_0, int_0, var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "Leonard"
    module_0.func()
