# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1437 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3836
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -3829
    module_1.object(*var_0, **var_0)
