# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1092 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"3"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bytes_0 = b""
    list_0 = [bool_0, bytes_0, bytes_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*var_0)


def test_case_3():
    bytes_0 = b"3"
    int_0 = 1131
    list_0 = [int_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    bytes_0 = b"2\t3"
    int_0 = 5
    list_0 = [
        int_0,
        bytes_0,
        bytes_0,
        bytes_0,
        int_0,
        int_0,
        int_0,
        bytes_0,
        bytes_0,
        bytes_0,
        int_0,
        bytes_0,
        bytes_0,
    ]
    var_0 = module_0.func(*list_0)
