# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_540 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "X,&p3730TG"
    bool_0 = True
    tuple_0 = (bool_0,)
    tuple_1 = (str_0, bool_0, tuple_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == 11
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = -1639.0492 - 3209j
    bytes_0 = b""
    set_0 = {complex_0, bytes_0}
    list_0 = [set_0, set_0, set_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "A"
    bool_0 = True
    tuple_0 = (bool_0,)
    tuple_1 = (str_0, bool_0, tuple_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == 1
    set_0 = {tuple_0, var_0}
    module_0.func(*set_0)