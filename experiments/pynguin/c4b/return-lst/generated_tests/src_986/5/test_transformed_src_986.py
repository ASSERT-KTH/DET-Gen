# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_986 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    complex_0 = -1110.9 + 2700.7071j
    list_0 = [bool_0, complex_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\xb8\x83\xaa\xaa\x17\xe5Qq\x98;\x00\xaf91"
    list_0 = [bool_0, bytes_0, bool_0, bytes_0]
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*list_0)
    bool_1 = False
#    module_0.func(*bool_1)
