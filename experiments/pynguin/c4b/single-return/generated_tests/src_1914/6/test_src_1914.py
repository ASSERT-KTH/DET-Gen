# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1914 as module_0


def test_case_0():
    str_0 = "EAww\n/>y["
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "EAww\n/>y["
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    module_0.func()


def test_case_3():
    str_0 = "rz=OwS~nrQV"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_4():
    str_0 = "c(Kt`GNgN]):!D9#EzJ"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_5():
    str_0 = "2oKK%)&{o!}s7Acgj\x0b"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_6():
    str_0 = "SCVKK{=$b]cGj\x0b"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_7():
    str_0 = "qCVVK~G\x0b"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
