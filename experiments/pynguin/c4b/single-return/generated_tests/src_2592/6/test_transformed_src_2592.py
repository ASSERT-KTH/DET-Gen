# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    list_0 = [dict_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x95),]\xb0\xb3\xc66\xaa\x9f\x94\n\xd5\x1a[\xd9\x92\x1fw"
    dict_0 = {bytes_0: bytes_0}
    list_0 = [dict_0, bytes_0, dict_0, dict_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "8s;2/{hW~N^mu."
    list_0 = [str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "999999999999"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 999999999999
    dict_0 = {}
    list_1 = [dict_0, dict_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "999^999999999"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 9989999999999
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "99&99999999"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 98999999999
    dict_0 = {}
    list_1 = [str_0, dict_0, dict_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 98999999999
    var_2 = module_0.func(*list_1)
    assert var_2 == 98999999999
#    module_0.func()
