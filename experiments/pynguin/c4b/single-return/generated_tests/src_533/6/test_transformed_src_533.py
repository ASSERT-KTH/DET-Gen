# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_533 as module_0


def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -276
    complex_0 = 7.438787 - 514.4j
    list_0 = [int_0, int_0, int_0, complex_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -276
    complex_0 = 7.438787 - 514.4j
    complex_1 = 1397 - 298.24742j
    list_0 = [complex_1, complex_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    list_1 = [int_0, int_0, int_0, complex_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
#    module_0.func()
