# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_420 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 1
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1381.4
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 438966041
    module_0.func()
