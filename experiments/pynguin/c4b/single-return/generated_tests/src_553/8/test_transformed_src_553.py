# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_553 as module_0


def test_case_0():
    bytes_0 = b"\x9b\xb4\x0cW\xf5\xbain\xbb"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 10


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'rY?Pu)aG]"j}+3*\t\t^'
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    bool_0 = True
    list_0 = [str_0, bool_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 17
    list_1 = []
#    module_0.func(*list_1)
