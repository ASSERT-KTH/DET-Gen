# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1665 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
    list_0 = [dict_0, tuple_0, dict_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
#    module_0.func(*list_0)


def test_case_2():
    str_0 = 'zzHj-*lk"TJWF,c{'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    dict_0 = {}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    complex_0 = -615.856385 - 435.059211j
    list_0 = [complex_0, complex_0, complex_0, complex_0]
    list_1 = [list_0, complex_0, list_0]
    var_0 = module_0.func(*list_1)
    bool_0 = False
    list_2 = [bool_0]
    list_3 = [list_2, bool_0, list_2]
    var_1 = module_0.func(*list_3)
#    module_0.func(*list_2)