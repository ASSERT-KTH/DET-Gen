# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1043 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 25
    bytes_0 = b"\x9a"
    set_0 = {int_0, bytes_0, bytes_0, bytes_0}
    str_0 = 'r\n0$)"8;GL'
    tuple_0 = (bytes_0, set_0, bytes_0, str_0)
    dict_0 = {int_0: int_0, int_0: tuple_0, str_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "Penny"
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "Sheldon"
#    module_0.func()
