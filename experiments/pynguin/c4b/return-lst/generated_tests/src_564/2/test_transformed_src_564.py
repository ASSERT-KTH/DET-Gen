# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_564 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"*\x85V\xa3aE8_\x9c\x962\xbf"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\xf9\xd4n\x18\x1b\x03\xad\x18\xff\x88vv\xb6\xb8kN "
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    bytes_0 = b"\xf9\xd4ny\x18\x1b\x03\xad\xffvv\xda-\xb8kN "
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, bytes_0, list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xf9\xd4ny\x18\x1b\x03\xad\xffvv\xda-\xb8kN "
    var_0 = module_1.object()
    list_0 = [
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        var_0,
        bytes_0,
        bytes_0,
    ]
    list_1 = [list_0, var_0, var_0, bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xf9\xd4ny\x18\x1b\x03\xad\xffvv\xda-\xb8kN "
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [
        bytes_0,
        bytes_0,
        bytes_0,
        list_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
    ]
    list_2 = [list_1, bytes_0, bytes_0, list_1]
    var_1 = module_0.func(*list_2)
#    module_0.func()
