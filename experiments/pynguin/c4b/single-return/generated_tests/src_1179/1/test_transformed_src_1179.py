# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1179 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"U\xd9^\x13?i("
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x94\x94\xa0\xbbm\xab\xcc^\xed\xc2\xaa"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func(*var_0)
