# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_112 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    int_0 = -16
    dict_0 = {bool_0: int_0}
    list_0 = [bool_0, dict_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 2000
    bytes_0 = b"'M\x10t6\xc89\xd1\x03\x9c\x1a\x99\x80\xf2"
    list_0 = [int_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1991
    bytes_0 = b"\xd4\xbb\xe0\xd2\x8blu+\x8e"
    list_0 = [int_0, int_0, int_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*list_0, **int_0)