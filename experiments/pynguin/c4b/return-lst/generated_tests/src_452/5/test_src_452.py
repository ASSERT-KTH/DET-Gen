# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_452 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1789.0
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()