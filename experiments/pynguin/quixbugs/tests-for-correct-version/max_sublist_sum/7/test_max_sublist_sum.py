# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    var_0 = module_0.max_sublist_sum(set_0)
    assert var_0 == 0
    none_type_0 = None
    module_0.max_sublist_sum(none_type_0)
