# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1047 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "4 6"
    bool_0 = False
    list_0 = [str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 4


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "84 6"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 9
#    module_0.func()
