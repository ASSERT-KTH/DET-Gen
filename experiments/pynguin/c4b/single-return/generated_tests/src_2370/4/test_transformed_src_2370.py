# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2370 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "'w=mg"
    tuple_0 = (str_0,)
    complex_0 = 3681.658505 + 770.90918j
    tuple_1 = (tuple_0, complex_0)
    list_0 = [tuple_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "'w=mg"
    tuple_0 = (str_0,)
    list_0 = [str_0, tuple_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "IGNORE HIM!"
#    module_0.func()
