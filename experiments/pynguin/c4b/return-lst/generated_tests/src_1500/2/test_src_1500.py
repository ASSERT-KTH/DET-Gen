# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1500 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1516
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()