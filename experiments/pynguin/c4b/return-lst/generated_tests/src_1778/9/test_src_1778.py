# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1778 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    str_0 = "*+"
    tuple_0 = (bool_0, str_0, bool_0)
    var_0 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bool_0 = True
    str_0 = "BB"
    list_0 = [bool_0, str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "BBB"
    list_0 = [bool_0, str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


def test_case_4():
    bool_0 = True
    str_0 = "u-BG'-,RRS=-E{NBXcL"
    list_0 = [bool_0, str_0, str_0, str_0, str_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    bool_0 = False
    str_0 = "u-GG`p,RYRS=-E{NBXcL"
    list_0 = [
        bool_0,
        str_0,
        str_0,
        str_0,
        bool_0,
        str_0,
        str_0,
        str_0,
        bool_0,
        bool_0,
        bool_0,
    ]
    var_0 = module_0.func(*list_0)


def test_case_6():
    bool_0 = True
    str_0 = "\rGGYtpRRRS=-\\NrX.L"
    list_0 = [bool_0, str_0, str_0, str_0, str_0, str_0, str_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_7():
    bool_0 = True
    str_0 = "GGGYpR/RS=-u%UrXgL"
    list_0 = [
        bool_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        bool_0,
        bool_0,
        bool_0,
        str_0,
        bool_0,
        bool_0,
    ]
    var_0 = module_0.func(*list_0)
