# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_528 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1691
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Leonard"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = {bool_0}
    bool_1 = True
    var_0 = module_0.func(*set_0)
    assert var_0 == "Sheldon"
    dict_0 = {bool_0: set_0, bool_0: set_0, bool_1: set_0, bool_0: set_0}
    list_0 = [dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
