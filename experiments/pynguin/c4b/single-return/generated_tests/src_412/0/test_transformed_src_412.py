# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_412 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x01\xb6C\xf4\xf78,\x7fx"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    object_0 = module_1.object()
    set_0 = {object_0}
    list_0 = [set_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "ad~g"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
#    module_0.func()
