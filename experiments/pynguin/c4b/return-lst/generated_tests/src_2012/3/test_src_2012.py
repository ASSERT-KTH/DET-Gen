# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2012 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    tuple_0 = (bool_0,)
    float_0 = 3324.324
    tuple_1 = (dict_0, tuple_0, float_0)
    list_0 = [tuple_1]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "_-4n)D\t"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    float_0 = -185.3
    list_1 = [float_0, float_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -218
    list_0 = [int_0, int_0, int_0, int_0]
    module_0.func(*list_0)
