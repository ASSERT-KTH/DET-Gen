# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2137 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    int_0 = -2717
    tuple_1 = (int_0, int_0, tuple_0, int_0)
    list_0 = [tuple_1, tuple_0, tuple_1]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"8K]\x00(\xcf\x03;"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0, bytes_0, list_0]
    bytes_1 = b"\x83\x97d"
    list_2 = [list_1, bytes_0, bytes_1, bytes_0]
    list_3 = [list_2, list_2, list_2]
    var_0 = module_0.func(*list_3)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"8K]\x00(\xcf\x03;"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0, bytes_0, list_0]
    bytes_1 = b"\x83\x97d"
    list_2 = [bytes_0, list_1, bytes_0, bytes_1, bytes_0]
    list_3 = [list_2, list_2, list_2]
    var_0 = module_0.func(*list_3)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"8K]\x00(\xcf\x03;"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0, bytes_0, list_0]
    var_0 = module_0.func(*list_0)
    bytes_1 = b"\x83\x97d"
    list_2 = [list_1, bytes_0, bytes_1, bytes_0]
    list_3 = [list_2, list_2, list_2]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_3)
#    module_0.func()