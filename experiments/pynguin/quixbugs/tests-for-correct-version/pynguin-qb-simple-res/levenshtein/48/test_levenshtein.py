# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "]m"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    none_type_0 = None
    module_0.levenshtein(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = 1092.458 - 99.49j
    module_0.levenshtein(complex_0, complex_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "FcQ7"
    var_0 = module_1.object()
    tuple_0 = (var_0, str_0, var_0, str_0)
    module_0.levenshtein(tuple_0, str_0)