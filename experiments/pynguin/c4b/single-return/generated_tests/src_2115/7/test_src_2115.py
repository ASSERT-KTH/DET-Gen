# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2115 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "??&iBOUJV\tRk+P%Yp5Pe"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    float_0 = -206.0
    module_0.func(*float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.func(*bool_0)
