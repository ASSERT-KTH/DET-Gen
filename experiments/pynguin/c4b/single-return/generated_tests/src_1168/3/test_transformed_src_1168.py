# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1168 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\r\xb9#\x8b\xba\x83T\xae(\x9c\xca\x9cG\xa8"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 56
#    module_0.func()


def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xa6C\xf9\xf1\x85\x13E\xb3J\x87\xf9e\xac\xc9\xc8\x19\xbbE\xbfB"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 231
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    float_0 = 656.90881
    list_0 = [bool_0, bool_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
#    module_0.func()
