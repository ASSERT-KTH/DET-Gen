# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2087 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    list_1 = [list_0, list_0]
    list_2 = [list_1, list_0]
    var_0 = module_0.func(*list_2)
    list_3 = []
#    module_0.func(*list_3)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc8\xbb\xe7\xd9\x91\xea\xe1W\xec \xb5\xcb\xb8\xee\xc0>}"
    list_0 = []
    list_1 = [bytes_0, bytes_0, bytes_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "?"
    float_0 = 2013.0
    list_0 = [str_0, float_0, float_0, float_0, str_0, str_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "?"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, list_0]
    var_1 = module_0.func(*list_1)
#    module_0.func()
