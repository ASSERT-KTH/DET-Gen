# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2295 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x19"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "IGNORE HIM!"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'p\xf8\x88\xff\xba\x82-Y\xc4C"y'
#    module_0.func(*bytes_0)
