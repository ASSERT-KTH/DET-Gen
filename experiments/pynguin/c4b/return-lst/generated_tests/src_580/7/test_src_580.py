# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_580 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -657
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 0
    dict_0 = {int_0: int_0}
    list_0 = [dict_0]
    var_0 = module_0.func(*dict_0)
    list_1 = [list_0, list_0, dict_0]
    module_0.func(*list_1)
