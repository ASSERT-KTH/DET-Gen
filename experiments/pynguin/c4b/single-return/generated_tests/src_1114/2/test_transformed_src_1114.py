# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1114 as module_0


def test_case_0():
    str_0 = "12w 5D\x0bzTt)-beU5"
    var_0 = module_0.func(*str_0)
    assert var_0 == "1"


def test_case_1():
    bytes_0 = b"\xdf\x17\x14\x99\xe8^\xba,"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa5\x12*\xd9Q\xdb\xfc\n\xf8\x9a\xf8E\xbc\x9d\x0e=7\x81\x98\xce"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "JdPf\r"
    var_0 = module_0.func(*str_0)
    assert var_0 == "j"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"z\xd2\x92\xdd\xb6S{}\xc8"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"Z\xd2\x92\xdd\xb6s{}\xc8"
    list_1 = [list_0]
    list_2 = [list_1, list_1]
#    module_0.func(*list_2)
