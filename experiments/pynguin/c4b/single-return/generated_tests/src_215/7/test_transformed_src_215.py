# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_215 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"\x16\xf3\xbeu\x03\xc3\x08\xeb\xfd\xab\xb45\xd3>\xf3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"/8\xf1gH\x0e\xd2\x10f\xcd\x9c;n4\xe9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x17\xf5\x0e\xc9\x82\xce\x97\xe4\xfc\xc3\x1d3\x15"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 14
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x8fyS?b\xa6\x8ey\x9b\xfb\xd2\xde-e\xe1"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_0.func()


def test_case_5():
    bytes_0 = b"\x81\xbdO\xa3\x00J #C\xee\x94"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
