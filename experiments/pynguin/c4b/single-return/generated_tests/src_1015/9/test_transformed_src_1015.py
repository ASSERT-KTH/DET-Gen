# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1015 as module_0


def test_case_0():
    str_0 = "i=@#Vx)WfR]]"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "rVVOuaR[jNFxDFz|"
    dict_0 = {str_0: str_0}
    list_0 = [str_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    list_1 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    var_2 = module_0.func(*str_0)
    assert var_2 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "i:AmKKV_^x_Wf[V]"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()