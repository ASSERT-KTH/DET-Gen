# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_934 as module_0


def test_case_0():
    int_0 = 2715
    bool_0 = False
    list_0 = [int_0, int_0, int_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 1
    module_0.func()


def test_case_3():
    int_0 = 2714
    bool_0 = False
    list_0 = [int_0, int_0, int_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7