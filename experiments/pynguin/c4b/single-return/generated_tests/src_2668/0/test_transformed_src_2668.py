# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2668 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
#    module_0.func(*list_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0"


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bool_0 = True
    bytes_0 = b"\x8aK\xeb1J\xbe\xe0Pz{!"
    list_0 = [bool_0, bytes_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0"
    list_1 = [bool_0, var_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "00"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "1"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    bool_0 = True
    bool_1 = False
    list_1 = [bool_0, var_0, bool_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == "1"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "10"
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)
