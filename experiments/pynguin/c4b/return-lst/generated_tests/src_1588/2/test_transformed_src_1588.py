# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1588 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


def test_case_4():
    bytes_0 = b"\x95\x1bG"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x1b"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"s"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()