# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_948 as module_0


def test_case_0():
    int_0 = 1406
    bool_0 = True
    list_0 = [bool_0, int_0, bool_0]
    tuple_0 = (int_0, bool_0, list_0)
    list_1 = [tuple_0, list_0, tuple_0, list_0]
    var_0 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
