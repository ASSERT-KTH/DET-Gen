# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1481 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "m(|v\x0c!OLSlp)I(-qJu\x0c"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -373
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1611
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_1.object(*var_0)
