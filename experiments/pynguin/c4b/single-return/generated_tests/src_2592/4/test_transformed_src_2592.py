# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0


def test_case_0():
    str_0 = "99999"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99999


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"m\x19\x85\xc4S\xef\xe9)\x96\xdeI\xa6E"
    list_0 = [bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "gF"
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "#8"
    list_0 = [str_0]
#    module_0.func(*list_0)


def test_case_5():
    str_0 = "999#9"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99899
