# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_412 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\rxhQ"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_1():
    str_0 = "4l"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"


def test_case_2():
    str_0 = "4l"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "z"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    object_0 = module_1.object()
    bool_0 = False
    set_0 = {str_0, bool_0, str_0}
    list_1 = [list_0, set_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    module_0.func()
