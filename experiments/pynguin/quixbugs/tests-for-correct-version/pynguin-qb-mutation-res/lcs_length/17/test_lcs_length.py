# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    bool_0 = False
    bool_1 = False
    set_0 = set()
    tuple_0 = (bool_1, set_0)
    tuple_1 = (bool_0, bool_0, bool_0, tuple_0)
    var_0 = module_0.lcs_length(tuple_1, tuple_1)
    assert var_0 == 4


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.lcs_length(dict_0, dict_0)
    assert var_0 == 0
    var_1 = module_0.lcs_length(dict_0, var_0)
    assert var_1 == 0
    module_0.lcs_length(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.lcs_length(bool_0, bool_0)