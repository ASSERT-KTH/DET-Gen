# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1102 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"I`j\xef\xd0)\xebY\xd5\x833\xf2v\xbe\x82\x93\xc9Z"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 33
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x7f\x06\xd5>\xcd\x8e\xdc4\xe8O\xe4K\xdd\xc9\xf6"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 33
#    module_0.func()