# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1529 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "$H=fm7\t~`L5erV%"
    var_0 = module_0.func(*str_0)
    assert var_0 == "$"
    object_0 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "r\x0b"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "r\x0b"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Hu=fme\t~`35er:x"
    var_0 = module_0.func(*str_0)
    assert var_0 == "h"
#    module_1.object(*var_0, **var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "p8#LDvq\\ 2u./.BN@]S"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "p8#LDvq\\ 2u./.BN@]S"
    var_1 = module_0.func(*str_0)
    assert var_1 == "P"
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "tW-[YHU'@Q~"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "Tw-[yhu'@q~"
    str_1 = 'M7|$Hu=f"m\x0b\t~`L5er:%'
    var_1 = module_0.func(*str_1)
    assert var_1 == "m"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "@H!=:#OVS[\x0b"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "@h!=:#ovs[\x0b"
    str_1 = '$Hu=f"m7\t~`L5er:%'
    var_1 = module_0.func(*str_1)
    assert var_1 == "$"
#    module_0.func()
