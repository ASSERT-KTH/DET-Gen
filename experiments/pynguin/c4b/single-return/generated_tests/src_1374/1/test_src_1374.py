# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1374 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1118.058612
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -280
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 605
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    complex_0 = -675 - 2589.699442j
    tuple_0 = (bool_0, bool_0, complex_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == -1
    module_1.object(*var_0, **var_0)
