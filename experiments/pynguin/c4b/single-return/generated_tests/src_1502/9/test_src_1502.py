# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1502 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1057
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "302 302"
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    assert var_1 == "302 302"
    var_2 = module_0.func(*var_1)
    assert var_2 == "0 2"
    var_3 = module_0.func(*var_0)
    assert var_3 == "0 2"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -195
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-54 -53"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -1
    list_0 = [int_0, int_0]
    list_1 = [int_0, int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "1 2"
    module_1.object(*list_0)
