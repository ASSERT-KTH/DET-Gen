# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2330 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"Nn\x96L-9t\x91g\x89\xd4\xdc\x9c\x8cxZ\xdaG"
    set_0 = {bytes_0, bytes_0}
    list_0 = [set_0, set_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


def test_case_1():
    str_0 = "LW"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "LW"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_0)
#    module_0.func()


def test_case_4():
    str_0 = "LW"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)


def test_case_5():
    str_0 = " D%UZ"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_6():
    str_0 = "vLW"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "<LW"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_3 = module_0.func(*var_2)
    var_4 = module_0.func(*var_0)
#    module_1.object(*var_3, **var_1)
