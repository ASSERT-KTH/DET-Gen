# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1163 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    list_1 = [list_0, list_0]
    tuple_0 = (list_0, list_1)
    list_2 = [tuple_0, list_1, list_0, list_0]
#    module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -2000.512802 + 4000.89292j
    list_0 = [complex_0, complex_0, complex_0]
#    module_0.func(*list_0)
