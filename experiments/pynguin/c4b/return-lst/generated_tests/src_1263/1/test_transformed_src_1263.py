# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1263 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"&JhW\x7f-P\x96c\x15\xa4\n\x1a|"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 4
    bool_0 = False
    list_0 = [bool_0, int_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*bool_0, **var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 4
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    bool_0 = False
    bytes_0 = b"\x03,\xda\xc3"
    var_1 = module_0.func(*bytes_0)
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    var_2 = module_0.func(*list_1)
#    module_0.func()
