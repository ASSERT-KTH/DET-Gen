# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1360 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2830
    bool_0 = False
    bool_1 = False
    tuple_0 = (int_0, bool_0, bool_1, int_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == -1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1545
    set_0 = {int_0, int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert (
        var_0
        == "444777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777"
    )
    module_0.func()
