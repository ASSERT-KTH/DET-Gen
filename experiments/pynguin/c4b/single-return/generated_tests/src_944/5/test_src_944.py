# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_944 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "qP_@36QV/G"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_1():
    str_0 = "4n|yoK}/ZM`VV"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = 'Oe"g\nw&\\KZ-DZLD_("S'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "IKDHea(0"
    list_0 = [str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    var_2 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "*g9+ C+K%KwSA\rx.oI"
    list_0 = [str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    object_0 = module_1.object()
    module_0.func()


def test_case_6():
    str_0 = "iVKVV"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2


def test_case_7():
    str_0 = "in|aoK(/ZM`VV"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_8():
    str_0 = "in|aoK(ZM`VV'"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_9():
    str_0 = "iOKVVK"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
