# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2552 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xef\x84Es\x06\xb9\xb9\x84\x9c\xbes\xbb5"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
#    module_0.func(*none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, bool_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1726
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()
