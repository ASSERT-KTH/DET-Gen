# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    set_0 = {tuple_0}
    int_0 = -477
    list_0 = [int_0, set_0, int_0]
    tuple_1 = (set_0, int_0, list_0)
    module_0.lis(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.lis(tuple_0)
    assert var_0 == 0
    module_0.lis(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "q-u0zk]&Z/P1asC"
    list_0 = [str_0, str_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1
    str_1 = "+_5WX|(`m~F"
    var_1 = module_0.lis(str_1)
    assert var_1 == 7
    var_2 = module_0.lis(str_1)
    assert var_2 == 7
    none_type_0 = None
    module_0.lis(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    bool_1 = False
    dict_0 = {bool_0: bool_1, bool_0: bool_0, bool_0: bool_1, bool_0: bool_1}
    tuple_0 = (bool_0, bool_0, bool_1, dict_0)
    module_0.lis(tuple_0)