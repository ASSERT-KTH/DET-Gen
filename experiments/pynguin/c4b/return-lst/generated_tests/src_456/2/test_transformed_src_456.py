# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_456 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"N"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1"
    var_0 = module_0.func(*str_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "0"
    var_0 = module_0.func(*str_0)
#    module_0.func()
