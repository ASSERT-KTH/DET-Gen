# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1914 as module_0


def test_case_0():
    str_0 = ">V\nj@Y\\Kh>N50,Mw9k\\"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "oSWX`9%cW]M"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    module_0.func()


def test_case_3():
    str_0 = ">V\nh@YKKh>N5@Mw9k\\"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ',r\rt[3wD\r6-t*j0DVVK"'
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()


def test_case_5():
    str_0 = ">VKK5@>BM"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
