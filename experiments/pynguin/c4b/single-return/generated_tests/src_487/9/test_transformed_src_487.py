# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_487 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "f\rsQ1E>l`_%iJx0$*\nW"
    var_0 = module_0.func(*str_0)
    assert var_0 == "F"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "f\rsQ1E>l`_%iJx0$*\nW"
    var_0 = module_0.func(*str_0)
    assert var_0 == "F"
    var_1 = module_0.func(*var_0)
    assert var_1 == "f"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "f\rsQ1E>l`_%iJx0$*\nW"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "f\rsQ1E>l`_%iJx0$*\nW"
    var_1 = module_1.object()
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ")\\A[WfH%N\n("
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ")\\A[WfH%N\n("
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "fQ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Fq"
#    module_0.func()
