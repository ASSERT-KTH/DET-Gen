# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1588 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_0, list_0, list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -15
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bytes_0 = b"\x8b\xcd\x17\xdf\xef\x11"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xcd\xdf"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


def test_case_5():
    bytes_0 = b"1\xf1\xb6)\xd2\x98i\n$*\xa8"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)
#    module_0.func()