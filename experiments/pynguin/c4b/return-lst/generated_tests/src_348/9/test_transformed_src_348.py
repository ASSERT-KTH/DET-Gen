# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_348 as module_0


def test_case_0():
    str_0 = "14"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0"
    int_0 = -1634
    list_0 = [str_0, str_0, int_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1"
    str_1 = "9"
    list_0 = [str_0, str_1]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
#    module_0.func()