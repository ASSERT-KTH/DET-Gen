# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_249 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Howard"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1772
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Leonard"
    str_0 = "tY\\wXy"
    tuple_0 = ()
    list_1 = [str_0, tuple_0, str_0]
    module_0.func(*list_1)
