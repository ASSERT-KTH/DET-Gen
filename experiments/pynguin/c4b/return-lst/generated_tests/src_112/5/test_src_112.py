# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_112 as module_0
import builtins as module_1


def test_case_0():
    float_0 = -1082.76626
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 346.0
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1531.11763
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
