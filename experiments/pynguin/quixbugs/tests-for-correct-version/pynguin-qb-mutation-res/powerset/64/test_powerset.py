# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import powerset as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1363
    module_0.powerset(int_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.powerset(bool_0)


def test_case_2():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    str_0 = 'wjw]O$Aa{#"gg\r[~'
    tuple_0 = (bool_0, set_0, str_0, bool_0)
    var_0 = module_0.powerset(tuple_0)