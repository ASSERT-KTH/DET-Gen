# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1321
    module_0.func(*int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    float_0 = 1686.42
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 999


def test_case_4():
    int_0 = 1927
    list_0 = [int_0, int_0, int_0, int_0]
    object_0 = module_1.object()
    var_0 = module_0.func(*list_0)
    assert var_0 == 1899


@pytest.mark.xfail(strict=True)
def test_case_5():
    object_0 = module_1.object()
    bytes_0 = b"iR\x9c\xc5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 99
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 1899
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1899
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    assert var_1 == 1899
    bytes_0 = b"l\x1a\xe9AE\xf3\xc5E"
    var_2 = module_0.func(*bytes_0)
    assert var_2 == 99
    module_0.func()
