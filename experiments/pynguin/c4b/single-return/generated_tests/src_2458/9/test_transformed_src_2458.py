# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2458 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb4\xe2M\xec=]&A\xde\xa0\xb5\xe9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    object_0 = module_1.object()
    list_0 = [var_0, var_0, var_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe2s\xec=\x8b&A\xde\xb5\xe9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    str_0 = "P}sZx"
    list_0 = [str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x04Q\x8acRh\xd8q\xc4\xb6\x8b\x1f\xfb\xe1\xf2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 21
    object_0 = module_1.object()
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 21
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x12\xbe:\x82^v\x81_i\x12\x11"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6
    var_1 = module_1.object()
#    module_0.func()
