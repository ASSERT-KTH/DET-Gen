# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_456 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe5\x9c\xfb\x11"
    bool_0 = False
    list_0 = [bytes_0, bytes_0, bool_0, bool_0, bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "8"
    var_0 = module_0.func(*str_0)
    assert var_0 == 16
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0
#    module_0.func(*var_0)
