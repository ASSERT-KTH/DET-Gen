# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1212 as module_0


def test_case_0():
    int_0 = 883
    list_0 = [int_0, int_0, int_0]
    list_1 = [list_0, list_0, int_0, list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.func(*list_0)


def test_case_2():
    bytes_0 = b"\xb5\x04\xc1\xddh\xd3\xd0"
    bool_0 = False
    bytes_1 = b'"\xa3\xb9A\xd0\xb6\xf1\x89\x1b\xe3\xbbl\xf3+\x18\xd7u\xa40\n'
    tuple_0 = (bytes_0, bool_0, bytes_1)
    var_0 = module_0.func(*tuple_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 883
    list_0 = [int_0, int_0, int_0]
    list_1 = [list_0, list_0, int_0, list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*var_0)
#    module_0.func()