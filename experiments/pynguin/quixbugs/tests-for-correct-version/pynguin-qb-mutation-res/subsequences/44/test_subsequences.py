# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    bool_1 = True
    var_0 = module_0.subsequences(bool_0, bool_1, bool_1)
    module_0.subsequences(bool_1, bool_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.subsequences(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1149
    module_0.subsequences(int_0, int_0, int_0)