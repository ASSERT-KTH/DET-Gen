# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2451 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "~whc}-&.tT)V4MnA"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 16
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xed\xa7L\xdfo,\xefRR\xee\t\xc7xo"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 13
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x0f\xdf!\xe5\xe7\x9aLc&\x9b\xd7\x8a"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 2
    list_2 = []
#    module_0.func(*list_2)
