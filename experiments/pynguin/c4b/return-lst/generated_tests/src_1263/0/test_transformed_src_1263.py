# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1263 as module_0


def test_case_0():
    bytes_0 = b"\x03/`\x04P\x8a[\xa0\x9a\x91\xa1V\xe2G\xb2\xc4"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bool_0, var_0]
    var_1 = module_0.func(*list_1)


def test_case_3():
    bytes_0 = b"\x03Mz\xa9\xd4\x04P\x8a\xa0\x9a\xa1V\xe2G\xb2\xc4"
    var_0 = module_0.func(*bytes_0)