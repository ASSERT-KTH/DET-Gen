# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2671 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x97"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "0.gm"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "3"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "V'0gF#m"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "24"
#    module_1.object(**str_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "0"
    list_0 = [str_0, str_0]
    object_0 = module_1.object()
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "00"
    var_1 = module_0.func(*var_0)
    assert var_1 == "0"
#    module_1.object(**list_1)
