# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2246 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b""
    list_0 = [bytes_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "IGNORE HIM!"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "N4"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
