# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    module_0.max_sublist_sum(list_0)


def test_case_1():
    bool_0 = True
    bool_1 = False
    tuple_0 = (bool_0, bool_1)
    var_0 = module_0.max_sublist_sum(tuple_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.max_sublist_sum(none_type_0)