# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_581 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x14\x9c\xe8"
    str_0 = '`NW&*s"3n\x0b8,X'
    tuple_0 = (bytes_0, str_0, str_0)
    list_0 = [tuple_0, tuple_0]
#    module_0.func(*list_0)


def test_case_1():
    str_0 = 'a@" R.*l\x0bNq@-DJee'
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    str_0 = '`NW&*s"3n\x0b8,X'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
