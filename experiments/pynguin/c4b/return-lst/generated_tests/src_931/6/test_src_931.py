# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_931 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\t"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "'?HN1D?HE;W\r'!Ow\\"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "M`}3U:oiIeM?"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\\.RF^\trw'n4ak$\rKE!:%"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "eRU;md>7DDS{hkQl?$e"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_0.func(*str_0)
    module_1.object(*list_0)