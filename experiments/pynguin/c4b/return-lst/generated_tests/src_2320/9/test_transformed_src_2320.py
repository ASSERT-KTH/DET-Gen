# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2320 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2575
    tuple_0 = (int_0,)
    dict_0 = {tuple_0: int_0}
    list_0 = [dict_0, tuple_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1B9wh9206Zu("
    var_0 = module_0.func(*str_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "u"
    var_0 = module_0.func(*str_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "1B9wh9206Zu("
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
#    module_0.func()
