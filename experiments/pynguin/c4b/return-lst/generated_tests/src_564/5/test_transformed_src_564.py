# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_564 as module_0


def test_case_0():
    bytes_0 = b"\x90\x9b\x10Fyq\xf7\xdcT\x985|q\xbf\x86[\t"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xc2@ll\xc7\x036wv\xfdN\x1a\xf9H\x8fe"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xc2@lll\x036wv\xfdN\x1a\xf9H\x8fe"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0, list_0, list_0, list_0, list_0, list_0, bool_0, list_0]
    list_2 = [list_1, list_1, bool_0, list_0]
    var_0 = module_0.func(*list_2)


def test_case_6():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    list_1 = [
        list_0,
        bool_0,
        list_0,
        list_0,
        list_0,
        list_0,
        list_0,
        list_0,
        list_0,
        bool_0,
        bool_0,
        list_0,
    ]
    list_2 = [list_1, list_1, bool_0, list_0]
    var_0 = module_0.func(*list_2)
