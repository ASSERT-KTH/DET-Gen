# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1447 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1037
    list_0 = [int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 1
    module_0.func()
