# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2553 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1236.3
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -594.415067
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    float_1 = 2449.384
    var_1 = module_0.func(*list_0)
    list_1 = [float_1, float_1]
    var_2 = module_0.func(*list_1)
    bool_0 = False
    module_0.func(*bool_0)