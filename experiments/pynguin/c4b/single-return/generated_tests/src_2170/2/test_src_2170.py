# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2170 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -570.0
    tuple_0 = (float_0, float_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 692775
    module_0.func()


def test_case_1():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
