# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1086 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 858.82451
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 214
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 857.7456086266345
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = [float_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_1.object(*var_0)
