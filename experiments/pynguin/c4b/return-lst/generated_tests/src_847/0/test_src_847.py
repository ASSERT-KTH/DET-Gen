# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_847 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    tuple_0 = (bool_0, dict_0, bool_0, bool_0)
    var_0 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    tuple_0 = (bool_0, dict_0, bool_0, bool_0)
    int_0 = 963
    list_0 = [int_0, tuple_0, tuple_0]
    module_0.func(*list_0)