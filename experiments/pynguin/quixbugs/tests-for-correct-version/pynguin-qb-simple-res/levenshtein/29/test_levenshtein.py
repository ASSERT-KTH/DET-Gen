# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "%wc@S*"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    float_0 = 6031.6055
    tuple_0 = (var_0, var_0, str_0, float_0)
    module_0.levenshtein(tuple_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1024
    module_0.levenshtein(int_0, int_0)