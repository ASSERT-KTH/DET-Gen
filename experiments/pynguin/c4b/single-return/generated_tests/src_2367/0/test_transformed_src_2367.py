# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2367 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -886
    bytes_0 = b""
    dict_0 = {bytes_0: bytes_0, int_0: bytes_0, bytes_0: int_0}
    tuple_0 = (int_0, bytes_0, dict_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "chest"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -858
    bytes_0 = b"0"
    dict_0 = {bytes_0: bytes_0, int_0: bytes_0, bytes_0: int_0, int_0: int_0}
    tuple_0 = (int_0, bytes_0, dict_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "chest"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -862
    bytes_0 = b"5"
    dict_0 = {bytes_0: bytes_0, int_0: bytes_0, bytes_0: int_0, int_0: int_0}
    tuple_0 = (int_0, bytes_0, dict_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "chest"
#    module_0.func()
