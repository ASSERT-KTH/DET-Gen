# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2330 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 505
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    list_0 = [dict_0, int_0, int_0, int_0]
    module_0.func(*list_0)


def test_case_1():
    str_0 = "9R_ij!yl,7TE/;"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "9R_ij!yl,7TE/;"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "H#/6"
    var_0 = module_0.func(*str_0)
    assert var_0 == "h"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "H#/6"
    list_1 = [list_0, list_0, list_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "H#/6"
    var_0 = module_0.func(*str_0)
    assert var_0 == "h"
    var_1 = module_0.func(*var_0)
    assert var_1 == "H"
    list_0 = [str_0, str_0, str_0, str_0]
    list_1 = [list_0, list_0, list_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "H#/6"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [list_0, list_0, list_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "J#/6"
    var_0 = module_0.func(*str_0)
    assert var_0 == "j"
    var_1 = module_0.func(*var_0)
    assert var_1 == "J"
    list_0 = [var_0, str_0, str_0, str_0, var_1, str_0, str_0, str_0]
    object_0 = module_1.object()
    list_1 = [list_0, object_0, list_0, list_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "#EY"
    var_0 = module_0.func(*str_0)
    assert var_0 == "#"
    var_1 = module_0.func(*var_0)
    assert var_1 == "#"
    list_0 = [str_0, str_0, var_0, str_0]
    var_2 = module_0.func(*list_0)
    assert var_2 == "#EY"
    module_0.func()
