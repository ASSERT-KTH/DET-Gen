# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_463 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "a:"
    var_0 = module_0.func(*str_0)
    assert var_0 == "A"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "a:"
    var_0 = module_0.func(*str_0)
    assert var_0 == "A"
    var_1 = module_0.func(*var_0)
    assert var_1 == "a"
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "#@FV)`Pj%k1h}]:-T"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "#@FV)`Pj%k1h}]:-T"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'c"R#L2U$'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 'C"r#l2u$'
    str_1 = "#@FV)`Pj%k1h}]:-T"
    var_1 = module_0.func(*str_1)
    assert var_1 == "#"
#    module_0.func()
