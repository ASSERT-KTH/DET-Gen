# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1651 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb4k$\xadK3\xcc\x16\x9b\xdf\xb1aU\xd5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Sheldon"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"K\x1c!\xee\xc2{S\xf8\xe8\xb0"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Howard"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == "Howard"
#    module_0.func()
