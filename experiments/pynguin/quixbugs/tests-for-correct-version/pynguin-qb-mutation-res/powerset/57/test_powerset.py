# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import powerset as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 373
    module_0.powerset(int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.powerset(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"b\x85"
    var_0 = module_0.powerset(bytes_0)
    list_0 = []
    var_1 = module_0.powerset(list_0)
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_2 = module_0.powerset(set_0)
    module_0.powerset(bool_0)