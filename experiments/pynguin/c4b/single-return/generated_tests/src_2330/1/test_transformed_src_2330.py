# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2330 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"f"
    int_0 = -1030
    list_0 = [bytes_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"F"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"d\x12\xe8\x9aNM\xe1}\x1f\x06\x95\xbc\x04\x0f"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "L6)?24G^s%Y?"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "L6)?24G^s%Y?"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\tF"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\tF"
    var_1 = module_0.func(*var_0)
    assert var_1 == "\t"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "\tF"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\tF"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "AF"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "af"
    var_1 = module_0.func(*var_0)
    assert var_1 == "A"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "xO"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Xo"
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    assert var_1 == "x"
    object_1 = module_1.object()
#    module_0.func()