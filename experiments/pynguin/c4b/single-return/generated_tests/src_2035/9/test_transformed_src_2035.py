# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2035 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
#    module_0.func(*none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "4HM}\rW"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "w4HM}NB\rW"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "KV"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_1.object(*var_0)
