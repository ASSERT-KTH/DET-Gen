# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "cMfE\x0bO(. d1X;gq=<"
    module_0.max_sublist_sum(str_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.max_sublist_sum(tuple_0)
    assert var_0 == 0
    set_0 = set()
    var_1 = module_0.max_sublist_sum(set_0)
    assert var_1 == 0
    var_2 = module_0.max_sublist_sum(tuple_0)
    assert var_2 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.max_sublist_sum(none_type_0)