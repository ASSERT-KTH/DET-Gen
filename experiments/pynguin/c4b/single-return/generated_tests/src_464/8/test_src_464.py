# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_464 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 15
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 575
    module_0.func(*int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
