# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.possible_change(list_0, bool_0)
    assert var_0 == 1
#    module_0.possible_change(var_0, var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
#    module_0.possible_change(none_type_0, none_type_0)


def test_case_2():
    bytes_0 = b"\xf1[>\xa7\x9c\x86\x1fK\xa2\xfb\xc8\x95\x1f\xd6="
    int_0 = -1185
    tuple_0 = (bytes_0, int_0)
    var_0 = module_0.possible_change(tuple_0, int_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.possible_change(bool_0, var_0)
    assert var_1 == 0
#    module_0.possible_change(var_0, var_0)
