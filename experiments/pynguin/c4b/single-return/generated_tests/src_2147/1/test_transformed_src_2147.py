# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2147 as module_0


def test_case_0():
    bytes_0 = b'\xb4\xa0y\xcd!\x885o\x81:\xc9"YF_\x9am(\x9c\xa6'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 803066


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    list_1 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    var_2 = module_0.func(*list_1)
    assert var_2 == 1
#    module_0.func()
