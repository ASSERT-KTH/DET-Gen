# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_60 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = [list_0, bool_0, list_0, bool_0, bool_0, list_0]
    var_0 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    str_0 = "nr&X'7Ud"
    list_0 = [str_0, str_0, object_0, object_0]
    var_0 = module_0.func(*list_0)
    object_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ">4i1SVMR{(nY"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    object_0 = module_1.object()
    str_0 = "4r&X'7Ud"
    list_0 = [str_0, object_0, str_0, str_0, object_0, object_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()