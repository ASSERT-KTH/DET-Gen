# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2054 as module_0


def test_case_0():
    bytes_0 = b"Js\xc920A\xbc\x84\xb9"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    int_0 = 1163
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()