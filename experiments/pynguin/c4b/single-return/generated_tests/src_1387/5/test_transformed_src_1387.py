# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1387 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    tuple_0 = ()
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_2():
    tuple_0 = ()
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*var_0)
    assert var_1 == "YES"


def test_case_3():
    str_0 = "Cc\x0b1!ZbI!a\\\rh@U<gE"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ";@0F}* O0D-"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    bytes_0 = b"J#-\x19"
    list_1 = [bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
#    module_0.func()
