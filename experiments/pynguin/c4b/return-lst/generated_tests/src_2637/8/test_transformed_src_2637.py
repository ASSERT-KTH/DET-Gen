# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2637 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -624
    tuple_0 = (int_0, int_0)
    bool_0 = True
    tuple_1 = (bool_0, int_0)
    dict_0 = {tuple_0: tuple_0, tuple_1: tuple_0}
    list_0 = [dict_0, dict_0, tuple_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"S#\x89D\xdct\xcb\xe2\xc4\xf9\x91\xc1\x12\x1f\x8f\xec\xb8+}\t"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_3():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x89Ws\x8b\x85\x0b\xc0\t\xc7\xfb\\u\x8b9\xf3\xc8"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "cJ"
    var_0 = module_0.func(*str_0)
#    module_0.func()
