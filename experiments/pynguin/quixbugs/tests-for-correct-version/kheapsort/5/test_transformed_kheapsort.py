# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xfa"
    var_0 = module_0.kheapsort(bytes_0, bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.kheapsort(list_0, bool_0)
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.kheapsort(list_0, bool_0)
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
#    module_1.object(*var_0)
