# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2528 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
#    module_0.func(*none_type_0)


def test_case_1():
    bool_0 = False
    bool_1 = True
    dict_0 = {bool_0: bool_0, bool_1: bool_1, bool_1: bool_1}
    list_0 = [bool_0, bool_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Reagan"
    var_1 = module_0.func(*list_0)
    assert var_1 == "Reagan"
