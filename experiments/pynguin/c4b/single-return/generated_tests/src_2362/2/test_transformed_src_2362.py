# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2362 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = '\x0bc8Y8w6W3U"0bP/Td1'
    var_0 = module_0.func(*str_0)
    assert var_0 == ".\x0b"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Y |/cJroxL"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    var_1 = module_1.object(*var_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = '\x0bc8Y8w6W3U"0bP/Td1'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.\x0b.c.8.8.w.6.w.3.".0.b.p./.t.d.1'
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
#    module_0.func()
