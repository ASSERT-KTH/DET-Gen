# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2095 as module_0


def test_case_0():
    complex_0 = 159.07942 + 1722.127619j
    dict_0 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
    list_0 = [dict_0, complex_0, dict_0, complex_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
#    module_0.func(*none_type_0)
