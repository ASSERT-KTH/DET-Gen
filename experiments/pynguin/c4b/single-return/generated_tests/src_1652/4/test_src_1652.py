# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1652 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 2550.95
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 583
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Xof*yG~NL*cbP"
    module_0.func(*str_0)
