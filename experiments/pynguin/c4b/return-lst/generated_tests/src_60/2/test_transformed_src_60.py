# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_60 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
#    module_0.func(*list_0)


def test_case_1():
    str_0 = "{UJ~MiJ"
    set_0 = {str_0}
    var_0 = module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '3(L Er7`?x;"S{'
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    var_1 = module_0.func(*str_0)
#    module_1.object(*tuple_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '3(L Er7`?x4"ur'
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    var_1 = module_0.func(*str_0)
#    module_0.func()
