# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_702 as module_0


def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    str_0 = "9&\\u5{2N1"
    tuple_0 = (bool_0, dict_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 3


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x92QD\xdd0\xe0\x05\x98\xa41/`&\x05%"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
