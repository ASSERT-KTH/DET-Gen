# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1311 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"\xf0\xdc\xcb\xb8b\xc3\x08\xf4\xf1A\xe8\x08\xf7\xcc\x02\xa7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf0\xdc\xb8bh\xc3\x08\xf4A\xe8\x08\xf7\x02\xa7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x820\xd8\x83W\x8f`\x1b\x80\xab\xdf\xeec\x0fN\xe5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xea]\x06\xe4\xca\xb9\xe9\x8cUrw\xb3^\xe0\x0f\xbf?]^\x0e"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 34
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"Q\xdc\xb8bh\xc3\x08\xf4A\xe8\x08\xf7\x02\xa7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_1.object(*var_0, **var_0)
