# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2394 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x98\x98T\x9a\x04\xa5\xdc\xcc\x87T\xea\t\xa8\xa1w"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd6\xac\x0cZ"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    list_1 = [list_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
    set_0 = {var_1}
    list_2 = [set_0, list_1, list_1, set_0]
    var_2 = module_0.func(*list_2)
    assert var_2 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "I4bh"
    dict_0 = {bool_0: bool_0, bool_0: bool_0, str_0: str_0, bool_0: bool_0}
    list_0 = [
        bool_0,
        str_0,
        dict_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        str_0,
        bool_0,
        dict_0,
        bool_0,
        dict_0,
    ]
    list_1 = [list_0, str_0, str_0, list_0, bool_0, dict_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"
    object_0 = module_1.object()
    var_2 = module_0.func(*var_0)
    assert var_2 == "NO"
    var_3 = module_0.func(*var_0)
    assert var_3 == "NO"
#    module_0.func(*object_0)
