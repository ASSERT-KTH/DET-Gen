# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_819 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 512
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1512
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -757
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 513
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 256
    module_1.object(*var_0, **var_0)
