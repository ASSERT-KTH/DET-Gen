# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2649 as module_0


def test_case_0():
    int_0 = -1492
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -747


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1325
    set_0 = {int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 662
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
