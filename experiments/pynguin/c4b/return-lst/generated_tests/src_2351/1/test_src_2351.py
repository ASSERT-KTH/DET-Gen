# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2351 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 921
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 922
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    list_1 = [bool_0, bool_0, dict_0, dict_0]
    var_1 = module_0.func(*list_1)
    object_0 = module_1.object()
    module_1.object(**var_1)