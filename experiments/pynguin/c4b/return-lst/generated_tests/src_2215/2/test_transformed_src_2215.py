# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2215 as module_0


def test_case_0():
    bytes_0 = b"\xb2\x12\x1fo'\xf2\x90\xbc\xdf\xeb\x0f&N\x02\x94q0\xd3N"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bytes_0 = b"\xb2\x12\x1fo'\xf2\x90\xbc\xdf\xeb\x0f&N\x02\x94q0\xd3N"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


def test_case_4():
    bytes_0 = b"\x96\xc2\xcb\xd2|\xbd"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
