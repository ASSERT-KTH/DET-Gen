# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -622.588058
    module_0.subsequences(float_0, float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bool_1 = True
    var_0 = module_0.subsequences(bool_0, bool_1, bool_1)
    bool_2 = True
    var_1 = module_0.subsequences(bool_2, bool_2, bool_2)
    dict_0 = {bool_2: bool_2}
    module_0.subsequences(dict_0, dict_0, bool_2)


def test_case_3():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)