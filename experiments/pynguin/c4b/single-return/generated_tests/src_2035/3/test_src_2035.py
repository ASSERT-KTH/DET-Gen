# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2035 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "i-0BlR\n+}}[~}c R[o"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    module_0.func()


def test_case_2():
    str_0 = "\t\x0c"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    object_0 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "KV"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    object_0 = module_1.object()
    module_0.func()
