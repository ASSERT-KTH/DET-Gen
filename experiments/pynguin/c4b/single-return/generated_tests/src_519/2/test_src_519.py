# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_519 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -352.62609
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 2242.60117
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Rajesh"
    module_0.func()
