# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_283 as module_0


def test_case_0():
    str_0 = "Wgf,0&\t\t\t"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "hh>z,="
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "h,0[Gel^lFo"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = module_0.func(*var_0)
    var_1 = module_0.func(*list_1)
#    module_0.func()
