# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1039 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "9M"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 31


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    str_0 = "98M"
    list_0 = [str_0, str_0, str_0, none_type_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 390
    var_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "83"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 22
#    module_0.func()
