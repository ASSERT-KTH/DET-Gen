# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1769 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\t6NuV8!"
    var_0 = module_0.func(*str_0)
    assert var_0 == "\t"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\t6Ne\\8!m"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\t6NE\\8!M"
    var_1 = module_0.func(*list_0)
    assert var_1 == "\t6NE\\8!M"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "rfPq\\--#QS"
    list_0 = module_0.func(*str_0)
    assert list_0 == "r"
    var_0 = module_0.func(*list_0)
    assert var_0 == "r"
#    module_1.object(*list_0)
