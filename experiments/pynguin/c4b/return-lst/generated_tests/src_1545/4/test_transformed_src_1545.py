# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1545 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"\xd5\x9f\x81\x0cW\x96y\x9f\xf1\x98_N"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    bytes_0 = b"\xd5\x9f\x81\x0cW\x96y\x9f\xf1\x98_N"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    list_1 = [var_0]
    var_2 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"ys$5\xe3Y\x1f.\xdbM\x1c"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    str_0 = "i\\X\x0cDj8/DraB6=?zU"
    tuple_0 = (list_0, str_0, bytes_0, str_0)
    var_0 = module_0.func(*tuple_0)
    var_1 = module_0.func(*list_0)
#    module_0.func()