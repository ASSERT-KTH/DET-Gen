# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2491 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "0\t0wQ-\x0c |3\x0cip"
    list_0 = [str_0]
#    module_0.func(*list_0)


def test_case_1():
    str_0 = "40776"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 780
    var_1 = module_0.func(*str_0)
    assert var_1 == -1


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "D.u"
    list_0 = [str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "40-3"
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)


def test_case_5():
    str_0 = "403"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "07476"
    var_0 = module_0.func(*str_0)
    assert var_0 == -1
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 753
#    module_0.func()


def test_case_7():
    str_0 = "407894718"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 894765
    object_0 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "4078947181"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 947596
#    module_1.object(*list_0)
