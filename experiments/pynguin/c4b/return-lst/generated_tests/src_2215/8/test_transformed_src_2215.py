# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2215 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "1en=\t\x0c%LZ"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xfcbe\xc37\x90LTV\xff\x90\xa2%\xce\xf5\x84U\x84E"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_3():
    bytes_0 = b"\xfcbe\xc37\x90LTV\xff\x90\xa2%\xce\xf5\x84U\x84E"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_1)


def test_case_4():
    bytes_0 = b"\x88\xc5\xf6J\xc7\xc7\xf6\x0bQ\xfb:\xdc\t"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    var_2 = module_0.func(*var_0)