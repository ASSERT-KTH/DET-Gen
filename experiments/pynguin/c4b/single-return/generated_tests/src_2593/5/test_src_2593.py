# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -979.30848
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -979
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 538
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 499
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 3717.7
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2999
    module_0.func(*var_0)


def test_case_4():
    float_0 = 172.9532828850894
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99
    object_0 = module_1.object()
    list_1 = [var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 99


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 1906.6428734759306
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1899
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"l\xf4_\x1dMwP\xd51\xf6@\x16L\x89\x88"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 99
    float_0 = 172.7
    list_0 = [float_0, float_0, float_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 99
    object_0 = module_1.object()
    module_0.func()
