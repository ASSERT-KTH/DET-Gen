# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_528 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 4127.95
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Rajesh"
    module_0.func()
