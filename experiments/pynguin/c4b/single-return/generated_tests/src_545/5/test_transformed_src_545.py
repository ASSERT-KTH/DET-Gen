# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_545 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "0Y&d%$`"
    var_0 = module_0.func(*str_0)
    assert var_0 == -1
#    module_0.func()


def test_case_2():
    bool_0 = True
    bytes_0 = b"\xa2\x16P*C\x87\xfb\xb2?\xbby@\xbc"
    set_0 = {bool_0, bool_0, bytes_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == -12
