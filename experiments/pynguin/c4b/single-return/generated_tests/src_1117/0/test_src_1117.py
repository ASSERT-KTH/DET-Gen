# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1117 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "0\t5"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    )


def test_case_2():
    str_0 = "uzJ4X$oG$O|=x"
    var_0 = module_0.func(*str_0)
    assert (
        var_0
        == 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    )


def test_case_3():
    str_0 = "0\t9\n5"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    )


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "+c\x0c*WNuD\rArYW/9rL2h~"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


def test_case_5():
    str_0 = "0 0\t9\n5"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
