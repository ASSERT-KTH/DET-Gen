# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0
import builtins as module_1


def test_case_0():
    int_0 = 3179
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "t\\}W3rb"
    str_1 = "oO \n$O"
    str_2 = "%"
    var_0 = module_0.lis(str_1)
    assert var_0 == 3
    dict_0 = {str_0: str_0, str_1: str_1, str_2: var_0, str_0: var_0}
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1
    none_type_0 = None
    module_0.lis(none_type_0)