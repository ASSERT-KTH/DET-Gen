# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_884 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1390.25
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcad\x9c"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xff\x02\xcad\\\x9c"
    var_0 = module_0.func(*bytes_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x99V&\x12\xbd\x16\x1e\\0j\xc3d&u\xee"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 892
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xff\x02\xcad\\\x9c"
    var_1 = module_0.func(*bytes_0)
    none_type_0 = None
#    module_0.func(*none_type_0)
