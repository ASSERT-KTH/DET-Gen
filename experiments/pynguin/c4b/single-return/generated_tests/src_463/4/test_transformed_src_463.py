# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_463 as module_0


def test_case_0():
    str_0 = "[w!e5\"'tXiT\\TFQ6?"
    var_0 = module_0.func(*str_0)
    assert var_0 == "["


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "[w!e5\"'tXiT\\TFQ?"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "[w!e5\"'tXiT\\TFQ?"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "bIT"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Bit"
    var_1 = module_0.func(*var_0)
    assert var_1 == "b"
    var_2 = module_0.func(*var_0)
    assert var_2 == "b"
#    module_0.func()
