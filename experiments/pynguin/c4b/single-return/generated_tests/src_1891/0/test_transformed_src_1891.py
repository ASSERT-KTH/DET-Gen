# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1891 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "p5\n1E"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "{|1\\D\t|?{m17zrVV\t~O"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_3():
    str_0 = "SW)? +[$<M`VK_&G7"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "KS))+V<$<Q`\tKK_&G7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "KKS))+V<$<M`VKV&`7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    var_1 = module_0.func(*list_0)
    assert var_1 == 2
    var_2 = module_0.func(*str_0)
    assert var_2 == 0
    var_3 = module_1.object()
    var_4 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "KS))+VK<$<M`VKV&`7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "KS)He)+VV$<M`VKV&`7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "KS)+VKk<$<Q`\tKK_&G7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "KS))+V<m<M`VKVV`7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
#    module_0.func()
