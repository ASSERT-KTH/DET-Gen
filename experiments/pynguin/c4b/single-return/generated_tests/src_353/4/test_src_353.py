# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_353 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    list_0 = [set_0, bool_0, bool_0, set_0]
    list_1 = [list_0, bool_0, set_0]
    tuple_0 = (bool_0, set_0, bool_0, list_1)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    list_0 = [set_0, bool_0, bool_0, set_0]
    list_1 = [list_0, bool_0, set_0]
    tuple_0 = (bool_0, set_0, bool_0, list_1)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0
    module_0.func()
