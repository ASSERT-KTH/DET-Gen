# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_466 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    str_0 = ""
    list_0 = [bool_0, str_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0"
    var_1 = module_0.func(*list_0)
    assert var_1 == "0"
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    str_0 = "F"
    list_0 = [bool_0, str_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "00"
    var_1 = module_0.func(*var_0)
    assert var_1 == "0"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    str_0 = "1"
    list_0 = [bool_0, str_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    object_0 = module_1.object()
    module_0.func()