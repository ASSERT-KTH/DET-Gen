# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_472 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "r>c_Jk^g!#\np9w8"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "KU_ynr\n"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "2_kCN[VV8\x0c;X"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
#    module_1.object(**var_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xde\xc0"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    str_0 = "Yeq\x0bV\x0cr"
    list_1 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "KV"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 0
    list_0 = [set_0, str_0, set_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "\\d\x0cX'S\tjSKKd=/,1c\x0b"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
