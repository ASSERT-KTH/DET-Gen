# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_806 as module_0


def test_case_0():
    bytes_0 = b"\x02\xb8\x1f&,\xa19\xaf\x1bl\x97\x97\xcd\x94r\xddy`\xd4\xff"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1743
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    int_0 = 115
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)