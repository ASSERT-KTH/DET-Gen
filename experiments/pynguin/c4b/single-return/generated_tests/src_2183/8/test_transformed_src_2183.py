# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2183 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe5\xaf\x18\xd9\x9e>\xb8t \x86\xc0^\xaf"
#    module_0.func(*bytes_0)


def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    list_1 = [bool_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"


def test_case_4():
    bool_0 = True
    bytes_0 = b"\x04\xa7B"
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    bytes_0 = b"\x04\xb2\xa7"
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    float_0 = 3189.341224
    list_1 = [float_0, bytes_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
    dict_0 = {var_0: list_0}
#    module_1.object(**dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    bytes_0 = b"\x07G\x89\x0e\xaen\x85\xb4T\x07\xc5O\x9e\x7f\xd5\x19{f\x9b"
    list_0 = [bool_0, bytes_0, bool_0, bytes_0]
    bool_1 = False
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    list_1 = [bool_1, bool_1, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
    var_2 = module_0.func(*list_1)
    assert var_2 == "YES"
    bytes_1 = b"\x04\x8f\xa7"
    list_2 = [bool_0, bytes_1]
    var_3 = module_0.func(*list_2)
    assert var_3 == "NO"
    var_4 = module_0.func(*list_0)
    assert var_4 == "NO"
#    module_0.func()
