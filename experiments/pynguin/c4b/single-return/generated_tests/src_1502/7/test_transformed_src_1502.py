# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1502 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 2076.5
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "592 594"
    list_1 = [var_0, float_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"c\xe4-\xeec\xb4\xd9oT\x05\xcd\x9bf#"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "28 29"
    str_0 = "mZ*m-ZyCM|:)s\tqw1Zl{"
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xfb\xb3}\xe7\x8aM\xf1\xe3\xf9F7\xd7S\xfbIW{ "
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "71 72"
#    module_0.func()
