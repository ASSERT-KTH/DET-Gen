# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 3168
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    module_0.subsequences(dict_0, dict_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)
    none_type_0 = None
    module_0.subsequences(none_type_0, bool_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    int_0 = 4524
    var_0 = module_0.subsequences(bool_0, int_0, bool_0)
    var_1 = module_0.subsequences(bool_0, bool_0, bool_0)
    none_type_0 = None
    module_0.subsequences(bool_0, bool_0, none_type_0)