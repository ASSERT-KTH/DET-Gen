# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1715 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 348
    set_0 = {int_0, int_0, int_0}
    list_0 = [int_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 232
    module_0.func()