# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_529 as module_0


def test_case_0():
    bytes_0 = b"M;W}\xb4"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.func(*dict_0)


def test_case_1():
    list_0 = []
    list_1 = [list_0]
    list_2 = [list_1, list_1, list_0]
    var_0 = module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bytes_0 = b'"\xf5WW\xd0\xc4\xd8w=\xce\x9bt'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b'"\xf5WW\xd0\xc4\xd8o=\xce\x9bt'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, bytes_0]
    var_1 = module_0.func(*list_1)
#    module_0.func()
