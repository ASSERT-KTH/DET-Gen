# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_402 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = True
    bytes_0 = b"\x88\x81\xaa\x96\x19J\xce\xb6\x90.4g"
    list_0 = [bool_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_2():
    str_0 = "84w[-A"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "87:4w[-\r"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = []
    list_1 = [bool_0, list_0, list_0, bool_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    str_0 = "84w[-A"
    var_1 = module_0.func(*str_0)
    assert var_1 == "NO"
    object_0 = module_1.object()
#    module_0.func(*var_1)
