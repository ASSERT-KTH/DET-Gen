# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1778 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "6#JR7xM"
    var_0 = module_0.func(*str_0)


def test_case_2():
    str_0 = '4RR%"t1B1)TtZsG'
    bool_0 = False
    list_0 = [bool_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = '.2TRR#"BB1TtZsG'
    bool_0 = True
    list_0 = [bool_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = '.2TRR#"BB1TtZsGG'
    bool_0 = True
    list_0 = [bool_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = '!`2?RRt#"BB1[sGGG'
    bool_0 = True
    list_0 = [bool_0, str_0, bool_0, str_0, bool_0, bool_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_6():
    str_0 = "`2lH&RRt#}BBB+t9,GG"
    bool_0 = True
    list_0 = [bool_0, str_0, str_0, str_0, bool_0, bool_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_7():
    str_0 = '.2TRRR#"BB1TtZsGG'
    bool_0 = False
    list_0 = [bool_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
