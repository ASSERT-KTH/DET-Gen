# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1021
    bool_0 = False
    tuple_0 = (int_0, int_0, bool_0)
    var_0 = module_0.kth(tuple_0, bool_0)
    assert var_0 is False
    none_type_0 = None
    module_0.kth(var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "{RT?{4Z`-aG~s}c|lCG["
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.kth(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1773
    tuple_0 = (int_0,)
    module_0.kth(tuple_0, int_0)