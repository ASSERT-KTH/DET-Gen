# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    module_0.possible_change(bool_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xec\x06`T\xc5\xda\xac\xa1\xd9\xca\x07u(\xc0\xde#A\x06\x0f\x97"
    module_0.possible_change(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2881
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    none_type_0 = None
    bool_0 = False
    module_0.possible_change(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 105.0
    module_0.possible_change(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    bool_0 = True
    var_0 = module_0.possible_change(tuple_0, bool_0)
    assert var_0 == 0
    module_0.possible_change(tuple_0, tuple_0)