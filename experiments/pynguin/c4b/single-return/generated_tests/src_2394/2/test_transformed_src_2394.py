# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2394 as module_0


def test_case_0():
    bytes_0 = b"\xd7u\xf5\x80\x80\x17E\xf8"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd7u\xf5\x80\x80\xf8"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"
    var_2 = module_0.func(*list_0)
    assert var_2 == "NO"
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0}
    list_0 = [
        set_0,
        bool_0,
        set_0,
        set_0,
        set_0,
        set_0,
        set_0,
        set_0,
        set_0,
        set_0,
        bool_0,
    ]
    list_1 = [list_0, bool_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
#    module_0.func()
