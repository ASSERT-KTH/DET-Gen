# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1778 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    int_0 = -396
    tuple_0 = (int_0,)
    list_0 = [int_0, tuple_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -397


def test_case_2():
    int_0 = 1899
    str_0 = '2"O~T5?qGBB:L'
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1887


def test_case_3():
    str_0 = "'2\"AqI|fGGR"
    bool_0 = False
    list_0 = [bool_0, str_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -10


def test_case_4():
    int_0 = 1799
    str_0 = "*7VsN[XY52ge)<RRS>4"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1781


def test_case_5():
    int_0 = -2136
    str_0 = "'X2N|ploBBB:R"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -2147


def test_case_6():
    str_0 = "'2\"AI|fGGGR"
    bool_0 = False
    list_0 = [bool_0, str_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -9


def test_case_7():
    int_0 = 2363
    str_0 = "*B7VsG[X52ge_<RRRSw4"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2345
