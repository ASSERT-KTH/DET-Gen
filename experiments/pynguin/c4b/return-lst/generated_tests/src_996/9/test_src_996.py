# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_996 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 4283
    bool_0 = False
    tuple_0 = (int_0, int_0, bool_0)
    list_0 = [tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
