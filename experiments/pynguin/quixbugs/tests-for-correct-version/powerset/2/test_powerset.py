# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import powerset as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.powerset(bool_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.powerset(none_type_0)


def test_case_2():
    bytes_0 = b"\x94\xdbLE$"
    str_0 = 'wP"`+w2I?H[@1'
    set_0 = set()
    tuple_0 = (bytes_0, str_0, set_0)
    var_0 = module_0.powerset(tuple_0)
