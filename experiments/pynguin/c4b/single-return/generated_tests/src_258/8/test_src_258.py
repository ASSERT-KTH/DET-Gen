# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_258 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    var_2 = module_0.func(*list_0)
    assert var_2 == 0
    list_1 = [var_0, var_0, var_0, var_0]
    module_0.func(*list_1)


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*list_0)
    assert var_1 == 1


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xdc\xe2\x0f\x03g\x01\x00U\xb3-5\xda/6G"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 34
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xdc\x01\x03g\x01\x00U-5\xda/G"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_1 = module_1.object()
    var_2 = module_0.func(*list_0)
    assert var_2 == 1
    module_0.func()
