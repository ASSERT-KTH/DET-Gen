# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_196 as module_0


def test_case_0():
    str_0 = "J\nbN(=9\tx[WA@zuj\x0c"
    var_0 = module_0.func(*str_0)
    assert var_0 == "0 0 0 0"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "J\nbN(=9\tx[WA@zuj\x0c"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "kIenJ1-[!Ij"
    list_0 = [str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "!"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"
    var_1 = module_0.func(*list_0)
    assert var_1 == "0 0 0 0"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ";g!Kfnkd-G\n\\{naa "
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)