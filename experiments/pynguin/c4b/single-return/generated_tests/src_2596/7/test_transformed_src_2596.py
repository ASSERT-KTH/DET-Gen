# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2596 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    list_1 = [var_0, bool_0, var_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "711"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1874
    dict_0 = {int_0: int_0, int_0: int_0}
    complex_0 = 6425.1344 - 2783.1822j
    bytes_0 = b"\xd6\x93\x98\x994A"
    tuple_0 = (complex_0, bytes_0)
    tuple_1 = (dict_0, complex_0, tuple_0, tuple_0)
    int_1 = 2248
    tuple_2 = (int_0, tuple_1, int_1)
    var_0 = module_0.func(*tuple_2)
    assert var_0 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
