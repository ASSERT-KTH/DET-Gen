# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1573 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "[gb\n'"
    var_0 = module_0.func(*str_0)
#    module_0.func()


def test_case_1():
    bytes_0 = b"^\xce\x95"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    str_0 = "VV"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "VK"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "KK"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_6():
    str_0 = "{J4QbKxdRCVE$9=?-"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "VVKR"
    list_1 = [str_1]
    var_1 = module_0.func(*list_1)


def test_case_7():
    str_0 = ">OVKK"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
