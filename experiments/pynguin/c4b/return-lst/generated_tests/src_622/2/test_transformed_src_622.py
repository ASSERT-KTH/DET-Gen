# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_622 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 925
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xf7\xf8\xc9l\x08\xe7"
    list_1 = [bytes_0, bytes_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, list_0, var_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
