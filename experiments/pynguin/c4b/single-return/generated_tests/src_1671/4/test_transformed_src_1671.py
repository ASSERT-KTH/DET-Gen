# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1671 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'"\xc6\xc2,\x18:+\xcc\xda'
    list_0 = [bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'Q]kB}"qg2'
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    var_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "@H~]2lH:d9kM1[*"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "Hjl< =zK\nTj"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    list_0 = [str_0, str_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 4
#    module_1.object(**var_0)
