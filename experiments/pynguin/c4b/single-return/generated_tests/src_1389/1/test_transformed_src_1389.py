# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1389 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xb9\xb6\x84\xa3j\x8d\x9d"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "8"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"IM\xb3\x92\xe5J\xc6\x84\x1d\xb1\x14\r"
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "wndSU>-G\\/"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "6"
    bytes_0 = b"\xb9\xb6\x84\xa3j\x8d\x9d\x9b( "
    set_0 = {bytes_0}
    list_1 = [bytes_0, bytes_0, bytes_0, set_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "11"
    list_2 = [bytes_0]
    var_2 = module_0.func(*list_2)
    assert var_2 == "11"
    object_0 = module_1.object()
#    module_0.func(*object_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4!|=>4CFLIrn8\rtRGj6"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "10"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "ndSU>-\\/O"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "5"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ";\x0cm-O8EIIb>[s\rs*\r_~"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "11"
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "/Y:qV4oY\x0c1w&0"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "6"
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "A^#i# )e q"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "10"
#    module_1.object(**var_0)