# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "ITvsS9qn\rX}=Ibn"
    module_0.max_sublist_sum(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.max_sublist_sum(list_0)
    assert var_0 == 0
    str_0 = "mC"
    module_0.max_sublist_sum(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 165
    module_0.max_sublist_sum(int_0)
