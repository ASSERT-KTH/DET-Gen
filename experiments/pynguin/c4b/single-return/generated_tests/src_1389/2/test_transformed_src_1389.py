# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1389 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "3"
    var_0 = module_0.func(*str_0)
    assert var_0 == "2"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "S6OY[ZEQMmNrg#4(v"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "11"
    var_1 = module_0.func(*var_0)
    assert var_1 == "2"
    var_2 = module_0.func(*var_1)
    assert var_2 == "2"
#    module_1.object(*var_2)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "As"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "2"
    var_1 = module_0.func(*var_0)
    assert var_1 == "2"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'I+#k"${*$+%:-#Uv77'
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "14"
    var_1 = module_0.func(*var_0)
    assert var_1 == "2"
#    module_0.func()
