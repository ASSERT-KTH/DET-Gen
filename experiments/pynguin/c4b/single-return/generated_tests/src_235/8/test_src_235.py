# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_235 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1632.83
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2856
    int_0 = 3431
    list_1 = [var_0, list_0, int_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
