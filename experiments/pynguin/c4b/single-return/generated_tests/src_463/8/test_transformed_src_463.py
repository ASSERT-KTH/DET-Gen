# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_463 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "/M\n[[\tc\t0x\r`L\x0c#Gg~"
    var_0 = module_0.func(*str_0)
    assert var_0 == "/"


def test_case_2():
    str_0 = " el?c;1G&"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == " el?c;1G&"


def test_case_3():
    str_0 = "AZoy2UGv=\x0b"
    var_0 = module_0.func(*str_0)
    assert var_0 == "a"
    list_0 = [var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "A"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b'y7#\xb1\xcd\x84\xb2\xc0M\xe6=ZSKC"\xa5U'
    list_0 = [bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "c3A/"
    int_0 = -1390
    set_0 = {str_0, int_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "C3a/"
#    module_0.func()
