# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2268 as module_0


def test_case_0():
    str_0 = 'i9EZ"\nKeAv3_jiW'
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = 'i9EZ"\nKeAv3iW'
    var_0 = module_0.func(*str_0)
    int_0 = 660
    list_0 = [str_0, int_0]
    var_1 = module_0.func(*list_0)
    list_1 = [var_1, list_0, var_1, list_0]
    var_2 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "HNlguJ)"
    var_0 = module_0.func(*str_0)
    int_0 = 660
    list_0 = [str_0, int_0]
    var_1 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "q;QV\\Za"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
#    module_0.func()
