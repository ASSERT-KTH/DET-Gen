# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1914 as module_0


def test_case_0():
    str_0 = "9GW\x0cSty\x0bb(K+_g3+f=;"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_1():
    str_0 = "hQGW\x0cS(KKM_f=V"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "9GW\x0cSty\x0bb(K+_g3+f=V"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_4():
    str_0 = "hQGW\x0cS(KKM_f=V"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_5():
    str_0 = "hQE\x0cCDS(VK_f=V"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_6():
    str_0 = "\n\\bos4^LJVV"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_7():
    str_0 = "\x0c:!h\x0cS(VKK`_"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_8():
    str_0 = "\x0cp!h\x0cSVVKK`_"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
