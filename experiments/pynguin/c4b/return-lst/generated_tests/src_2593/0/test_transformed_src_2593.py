# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    bytes_0 = b"g\x95;\x0e\x8c\xd7iZ"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\xd8}"
    var_0 = module_0.func(*bytes_0)


def test_case_3():
    bytes_0 = b"g\x95;\x0e\x8c\xd7iZ"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xbdy\xc1\x19X\xca\x06\x9e\x99\xda\xa6Ei\xcf\xfb`\x13"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 1853
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xbdy\xc1\x19X\xca\x06\x9e\x99\xda\xa6Ei\xcf\xfb`\x13"
    var_1 = module_0.func(*bytes_0)
    object_0 = module_1.object()
#    module_0.func()


def test_case_6():
    bytes_0 = b"l\xa6@<"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
    var_2 = module_0.func(*var_0)
    object_0 = module_1.object()