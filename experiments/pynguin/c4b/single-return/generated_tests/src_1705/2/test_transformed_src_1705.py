# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1705 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"`\xa1\xda#\x00\x01"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bytes_0 = b'";\xfc\xd3\xfe>A\xf4'
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"`\xa1\x00\x01"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 96
#    module_0.func(*var_0)
