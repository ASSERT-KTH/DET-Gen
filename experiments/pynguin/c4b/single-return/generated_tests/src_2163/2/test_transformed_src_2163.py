# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2163 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"i\xe8\xd8\xe6\x86\xc9$\x02\xba\xda\x13\xe7{\x89\xb8\xcd\xed\x07\x9b"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    var_2 = module_0.func(*list_0)
    assert var_2 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "yr<GK#l?/GWk7R"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "yr<GK#l?/GWk7R"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    list_1 = [list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 3
#    module_0.func()
