# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_44 as module_1


def test_case_0():
    object_0 = module_0.object()
    bool_0 = True
    set_0 = {object_0, object_0, object_0, bool_0}
    var_0 = module_1.func(*set_0)
    list_0 = [var_0, set_0, var_0]
    module_1.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 4746
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_1.func(*list_0)
    module_1.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 868
    list_0 = [int_0]
    var_0 = module_1.func(*list_0)
    int_1 = 3
    list_1 = [int_1, int_1, int_1, int_1]
    var_1 = module_1.func(*list_1)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 137
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_1.func(*list_0)
    object_0 = module_0.object()
    var_1 = module_0.object()
    module_1.func()
