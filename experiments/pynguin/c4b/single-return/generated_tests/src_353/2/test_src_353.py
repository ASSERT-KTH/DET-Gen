# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_353 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 135
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 27
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1811
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -362
    module_0.func(*int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
