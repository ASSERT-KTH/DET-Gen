# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_472 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "O{ QVsmOW~KH\t6n"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "O{ QVsmOW~KH\t6n"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0;"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "KV"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
#    module_1.object(*var_1, **var_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "O{&VVsmOa~KH\t6 &"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    object_0 = module_1.object()
    var_2 = module_0.func(*list_0)
    assert var_2 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = '9"JGy6F:14KK['
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
