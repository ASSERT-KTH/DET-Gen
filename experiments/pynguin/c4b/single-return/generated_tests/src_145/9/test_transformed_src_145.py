# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 3577
#    module_0.func(*int_0)


def test_case_2():
    float_0 = -2871.192
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3


def test_case_3():
    bytes_0 = b"\x17\x03\xaf"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1


def test_case_4():
    float_0 = -2871.192
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    bytes_0 = b"\x9b%"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 3
    var_2 = module_0.func(*list_0)
    assert var_2 == 3


def test_case_5():
    bytes_0 = b"\x10\x1fWf\x14\x05}\xe1NJ"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2


def test_case_6():
    float_0 = 39.0
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    bytes_0 = b"\x17\x03\xaf"
    list_1 = [float_0]
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 1
    var_2 = module_0.func(*list_1)
    assert var_2 == 2


def test_case_7():
    float_0 = -2896.978852964562
    bytes_0 = b"\x17\x03\xaf"
    list_0 = [float_0]
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    var_1 = module_0.func(*list_0)
    assert var_1 == 2
    int_0 = 1925
    list_1 = [var_1, list_0, list_0, int_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == 1