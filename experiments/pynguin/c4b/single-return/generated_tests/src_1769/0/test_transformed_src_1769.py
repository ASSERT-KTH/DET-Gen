# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1769 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\x0c\\n!Mm%"
    var_0 = module_0.func(*str_0)
    assert var_0 == "\x0c"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Dv9\r8xI45FP-j%}7"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "DV9\r8XI45FP-J%}7"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "wE~0j$o18"
    list_0 = module_0.func(*str_0)
    assert list_0 == "w"
    var_0 = module_0.func(*list_0)
    assert var_0 == "w"
#    module_0.func()
