# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1572 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "?2O:"
    tuple_0 = ()
    int_0 = 1816
    tuple_1 = (str_0, tuple_0, int_0)
    set_0 = {tuple_1, int_0, int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    int_0 = 1816
    tuple_1 = (tuple_0, tuple_0, int_0)
    set_0 = {tuple_1, int_0, int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 1
    module_1.object(*var_0, **var_0)
