# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2137 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    int_0 = 360
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    list_1 = [list_0, list_0, list_0, int_0, list_0, list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\x0c};\t\x0c[11d1(e"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = 'QSb4\x0c")Nt}A]'
    bool_1 = True
    tuple_0 = (bool_0, str_0, bool_1)
    list_0 = [tuple_0, bool_1]
    bytes_0 = b"\xda\x1e\x98\xe3d\x0b:\xe3\xd0\xb4wC\x96-|\x91f\xc6j\x0b"
    list_1 = [list_0, bytes_0, bytes_0]
#    module_0.func(*list_1)
