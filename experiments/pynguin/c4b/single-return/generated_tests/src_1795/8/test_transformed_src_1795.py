# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1795 as module_0


def test_case_0():
    str_0 = "PCX`YNR"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "~Eq_\t UU1ibO"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
#    module_0.func()


def test_case_3():
    str_0 = "PCX`YNR"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "A|qgGJ3cz*R>,~Qi\tY'\x0b"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 17
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "~EE_\t UU1IbO"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 4
#    module_0.func()
