# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2320 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Zc6yV]1(\t+UKe"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".z.c.6.v.].1.(.\t.+.k"
#    module_0.func()


def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "."
    bytes_0 = b"\x977\x1a\x8d\x92I,,\xbdJ\xb2\xa1\x92\xadi\x91\x9c\xe8"
    list_1 = [set_0, bytes_0, bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "."


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
