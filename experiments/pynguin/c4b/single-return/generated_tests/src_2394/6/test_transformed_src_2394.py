# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2394 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Li Sp\\3"
    int_0 = -2905
    list_0 = [str_0, str_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "CBK^`iiB`YMOs"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -206.49062177861657
    bool_0 = True
    list_0 = [
        bool_0,
        float_0,
        float_0,
        float_0,
        float_0,
        float_0,
        float_0,
        float_0,
        bool_0,
    ]
    list_1 = [list_0, bool_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
#    module_1.object(*list_1, **var_0)
