# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1523 as module_0


def test_case_0():
    float_0 = -643.791
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.func(*none_type_0)


def test_case_3():
    bool_0 = False
    set_0 = set()
    tuple_0 = (bool_0, bool_0, set_0)
    list_0 = [tuple_0, tuple_0, set_0, tuple_0]
    var_0 = module_0.func(*list_0)