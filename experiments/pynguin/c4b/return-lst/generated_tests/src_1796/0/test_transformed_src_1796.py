# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1796 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    int_0 = 1748
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"#*\x8a\xa1\xb9\xd9\x0e\xb8q"
    var_0 = module_0.func(*bytes_0)
#    module_1.object(*var_0, **var_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\t*\xc1\xb9\xb6\x0erq"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x16\x98\x01"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()
