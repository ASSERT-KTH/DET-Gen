# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2012 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 287
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    list_0 = [dict_0, dict_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "*i5\n ahZ#To"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 11
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
