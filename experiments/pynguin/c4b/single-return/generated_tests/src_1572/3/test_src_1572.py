# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1572 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "6Lzy.\x0c"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


def test_case_2():
    str_0 = "6Lz{y\x0c"
    int_0 = 2458
    list_0 = [int_0, str_0, str_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "-ibZ\\FFmZ"
    int_0 = 2458
    list_0 = [int_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    object_0 = module_1.object()
    list_1 = [str_0, var_0]
    module_0.func(*list_1)
