# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1398 as module_0
import builtins as module_1


def test_case_0():
    int_0 = -1194
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)


def test_case_2():
    float_0 = -4612.4644873083025
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_1.object()
