# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1015 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "!{RymMi"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "VVy1tfDWzo9t$y5)w"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '4Y\\"VH9KK(\x0bwh2n05njF'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
