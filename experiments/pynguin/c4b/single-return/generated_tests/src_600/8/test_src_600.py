# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_600 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "77\r7"
    set_0 = {str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 973
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "7\r7"
    set_0 = {str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 21
    module_1.object(*var_0)
