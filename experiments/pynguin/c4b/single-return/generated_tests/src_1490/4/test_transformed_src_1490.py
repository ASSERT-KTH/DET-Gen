# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1490 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    str_0 = "Q>MY48\x0b\\zHt"
    tuple_0 = (set_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Q>MY48\x0b\\zHt"
    tuple_0 = (str_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "YES"
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    str_0 = "Q>MY48\x0b\\zHt"
    tuple_0 = (set_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"
    var_2 = module_0.func(*var_1)
    assert var_2 == "NO"
    var_3 = module_0.func(*var_2)
    assert var_3 == "NO"
#    module_0.func()
