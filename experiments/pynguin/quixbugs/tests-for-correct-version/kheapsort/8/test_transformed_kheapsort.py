# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.kheapsort(none_type_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    var_0 = module_0.kheapsort(none_type_0, none_type_0)
    bool_0 = False
    var_1 = module_0.kheapsort(none_type_0, var_0)
    list_0 = [bool_0, bool_0, bool_0]
    var_2 = module_0.kheapsort(list_0, bool_0)
#    module_1.object(*var_2)
