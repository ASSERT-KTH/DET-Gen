# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1994 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -12
    dict_0 = {int_0: int_0}
    list_0 = [dict_0]
    module_0.func(*list_0)


def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
