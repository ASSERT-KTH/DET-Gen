# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "WI$%2Fa"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ">9#>7WVE"
    int_0 = -153
    module_0.kth(str_0, int_0)


def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.kth(dict_0, bool_0)
    assert var_0 is False
    bool_1 = False
    var_1 = module_0.kth(dict_0, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.kth(dict_0, bool_0)
    assert var_0 is False
    bool_1 = True
    module_0.kth(dict_0, bool_1)