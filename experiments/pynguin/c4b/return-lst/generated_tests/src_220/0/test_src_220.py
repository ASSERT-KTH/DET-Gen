# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_220 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -551
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 639
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 668
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    list_1 = []
    object_0 = module_1.object()
    module_0.func(*list_1)
