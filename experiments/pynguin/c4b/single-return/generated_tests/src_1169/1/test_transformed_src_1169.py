# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1169 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 3109
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5008539929
    none_type_0 = None
    list_1 = [none_type_0, none_type_0, none_type_0, none_type_0]
#    module_0.func(*list_1)
