# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1572 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    int_0 = -1549
    list_0 = [int_0]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 0


def test_case_2():
    int_0 = -1525
    list_0 = [int_0, int_0]
    list_1 = [int_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1


def test_case_3():
    int_0 = -1549
    list_0 = [int_0, int_0, int_0]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 2
    list_2 = [int_0, list_1, list_0]
    var_1 = module_0.func(*list_2)
    assert var_1 == 0
    object_0 = module_1.object()