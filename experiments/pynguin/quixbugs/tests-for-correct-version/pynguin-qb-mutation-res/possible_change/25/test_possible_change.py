# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.possible_change(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    int_0 = -1480
    var_0 = module_0.possible_change(bool_0, int_0)
    assert var_0 == 0
    bytes_0 = b"5\x00^\x0e\x1cS\x9chP9\xd5\x8a\x83\xf5h\xa9\xba\xb2\xe7\x16"
    none_type_0 = None
    module_0.possible_change(none_type_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2065
    module_0.possible_change(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.possible_change(var_0, bool_0)
    assert var_1 == 1
    complex_0 = 1152.6 - 113.55j
    set_0 = {var_1, complex_0}
    dict_0 = {var_1: bool_0, var_0: set_0}
    var_2 = module_0.possible_change(dict_0, var_0)
    assert var_2 == 1
    module_0.possible_change(complex_0, complex_0)