# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_814 as module_0


def test_case_0():
    bytes_0 = b"$\xe8\x1b\xcf\x06\xd1\x02\xed\xd4\xee\x8d\xbc\xcc\x18"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "447777"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\x065<\x86\x14\x85\x1cel\xea,\xbf\x08\xa5\xf6t\x0b$\xe0\x1a"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "-1"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1"
    bool_1 = True
    list_1 = [bool_1, bool_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == "-1"
    list_2 = [var_0, var_1, var_0]
    var_2 = module_0.func(*list_2)
    assert var_2 == "-1"
#    module_0.func(*var_1)
