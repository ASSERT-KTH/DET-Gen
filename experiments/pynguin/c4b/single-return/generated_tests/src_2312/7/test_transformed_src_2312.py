# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2312 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'f1\xae\x13\xe3\xe1a\r\xe2=\x0f\xff\xf8\x92"|\xb7'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


def test_case_1():
    dict_0 = {}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "&Sy[]R'*S\x0cW8'zPtH"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".&"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "&Sy[]R'*S\x0cW8'zPtH"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".&.s.[.].r.'.*.s.\x0c.w.8.'.z.p.t.h"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".&"
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
    object_0 = module_1.object()
#    module_0.func()