# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2089 as module_0


def test_case_0():
    bytes_0 = b"\x1c\x90\xa7\xe0\xec\xc9\x8a\xd0\x16\xa9\x00LL\x01\x80 lN\xa7"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -466
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    list_1 = [list_0, list_0, int_0, int_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func(*var_0)