# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9c"
    list_0 = [bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "vm"
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "{}9"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)


def test_case_4():
    str_0 = "73L9"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 6999


def test_case_5():
    str_0 = "79=9"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7899


def test_case_6():
    str_0 = "799#"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7989
