# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_381 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"Y\x87\xae"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "9"
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa2\xbf\xea"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "8"
    object_0 = module_1.object()
#    module_1.object(**var_0)
