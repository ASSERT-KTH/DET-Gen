# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_328 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "<)[\rw3A:UR_=`U\nk"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "T[=V>xkfi1UA_c~G/"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "T[=V>xkfi1UA_c~G/"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    list_0 = [str_0, str_0, str_0, str_0]
    var_2 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ""
    dict_0 = {str_0: str_0}
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [dict_0, str_0]
#    module_1.object(*list_1, **var_0)