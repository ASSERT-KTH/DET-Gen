# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_812 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    set_0 = {var_0}
    set_1 = {var_0, var_0}
    list_1 = [set_0, set_1, list_0, list_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"2mry\xd7Z"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Leonard"
#    module_0.func()
