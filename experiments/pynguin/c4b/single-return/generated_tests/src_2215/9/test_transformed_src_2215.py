# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2215 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "SiUOquviejBuP"
    list_0 = [str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    tuple_0 = (bool_0,)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xfc\xd1C\xe6G\xb5\x11\xba"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "252209672307118117186"
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\xfc\xd1C\xe6G\xb5\x11\xba"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "252209672307118117186"
    list_1 = [var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "199999999999999999999"
#    module_0.func()
