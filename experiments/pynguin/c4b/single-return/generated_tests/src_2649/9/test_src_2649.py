# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2649 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1864
    list_0 = [int_0, int_0, int_0, int_0]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 931
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 0
    module_0.func()
