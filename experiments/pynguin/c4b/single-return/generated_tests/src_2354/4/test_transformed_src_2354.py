# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2354 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xfb\xde\x94\x0c\x00\x05\x97"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "`:$o>"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".`"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "`:$o>"
    dict_0 = {str_0: str_0}
    var_0 = module_0.func(*str_0)
    assert var_0 == ".`"
    var_1 = module_0.func(*dict_0)
    assert var_1 == ".`.:.$.>"
    var_2 = module_0.func(*dict_0)
    assert var_2 == ".`.:.$.>"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ""
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    str_1 = "`:$o>"
    var_1 = module_0.func(*str_1)
    assert var_1 == ".`"
#    module_0.func()
