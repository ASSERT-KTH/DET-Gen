# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1545 as module_0


def test_case_0():
    bytes_0 = b"\x96\xcf\xa3\xa7X\xbc\xb5\xd7,{\xc7\xee\x91\xb2\x08\x84\xfa\xb4\x07"
    tuple_0 = (bytes_0, bytes_0, bytes_0, bytes_0)
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\x96\xcf\xa3\xa7X\xbc\xb5\xd7,{\xc7\xee\x91\xb2\x08\x84\xfa\xb4\x07"
    tuple_0 = (bytes_0, bytes_0, bytes_0, bytes_0)
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*tuple_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x96\xcf\xa3\xa7X\xbc\xb5\xd7,{\xc7\xee\x91\xb2\x08\x84\xfa\t\xb4\x07"
    tuple_0 = (bytes_0, bytes_0, bytes_0, bytes_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0]
    list_1 = [list_0, bytes_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()
