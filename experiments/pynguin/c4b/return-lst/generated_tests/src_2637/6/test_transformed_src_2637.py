# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2637 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "gF6i/CsC"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_1)
#    module_0.func()


def test_case_1():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "gF6i/CsC"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, list_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*str_0)
    var_3 = module_0.func(*var_2)
#    module_0.func()
