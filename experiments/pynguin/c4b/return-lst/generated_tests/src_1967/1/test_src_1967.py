# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1967 as module_0


def test_case_0():
    str_0 = "VIZ2V"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "d4me21xWJKKc>pW4~79q"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "d4me1xWJKKc>pW44~79"
    list_0 = []
    list_1 = [str_0, str_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "d4m71xJKKc*4p4nW44~7"
    list_0 = []
    list_1 = [str_0, str_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func(*list_0)
