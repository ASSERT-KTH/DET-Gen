# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


def test_case_0():
    str_0 = "0\t"
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)


def test_case_1():
    int_0 = 311
    dict_0 = {int_0: int_0, int_0: int_0}
    var_0 = module_0.wrap(dict_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.wrap(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    str_0 = "9<Vd?O)%SdX"
    var_0 = module_0.wrap(str_0, bool_0)
    module_0.wrap(bool_0, var_0)