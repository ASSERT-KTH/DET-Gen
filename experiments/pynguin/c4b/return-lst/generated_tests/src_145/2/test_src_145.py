# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0
import builtins as module_1


def test_case_0():
    float_0 = 471.39
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -532.453
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 474.7494
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0, **var_0)


def test_case_4():
    float_0 = 471.386
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_0.func(*var_0)


def test_case_5():
    float_0 = 445.8728303913943
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_1.object()
    object_0 = module_1.object()
