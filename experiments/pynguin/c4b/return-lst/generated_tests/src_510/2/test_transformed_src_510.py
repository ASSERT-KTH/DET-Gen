# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_510 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    list_0 = [bool_0, bool_0, bool_0, set_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_1():
    bool_0 = True
    bytes_0 = b"\xfa\x02\x92"
    bytes_1 = b"\xf3\xa9\x8e$c\xbbP\xe2/\xf0\xe6\xce5~"
    list_0 = [bool_0, bytes_0, bytes_1, bytes_1]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1667
    complex_0 = 75.300445 + 452.715723j
    set_0 = {int_0, complex_0}
    var_0 = module_0.func(*set_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 1176.54001
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_0)
#    module_0.func()
