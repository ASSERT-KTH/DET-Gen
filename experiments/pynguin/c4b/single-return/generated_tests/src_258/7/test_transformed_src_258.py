# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_258 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xd0b\xe1oP\xafG\xf2\x7fH\xfc\x8b\x88V'\xdc\xc8\xd4|"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xd0b\xe1o\xbbPG\xf2\x7fH\xfc\x8b\x88V'\xdc\xc8\xd4|"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xd0b\x19oP\xfbG\xf2\x7fH\xfc\x8b\x88V'\xdc\xc8\xd4|"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
#    module_1.object(**var_0)
