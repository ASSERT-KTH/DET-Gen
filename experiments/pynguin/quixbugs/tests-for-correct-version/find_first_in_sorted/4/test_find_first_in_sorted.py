# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9dT.\xe13&\x94\x81\x11^\xcaf\x9a"
    module_0.find_first_in_sorted(bytes_0, bytes_0)


def test_case_1():
    bytes_0 = b""
    var_0 = module_0.find_first_in_sorted(bytes_0, bytes_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "M"
    set_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert set_0 == 0
    module_0.find_first_in_sorted(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "M"
    int_0 = 312
    tuple_0 = (int_0,)
    tuple_1 = (int_0, tuple_0)
    var_0 = module_0.find_first_in_sorted(tuple_1, tuple_0)
    assert var_0 == 1
    var_1 = module_1.object()
    var_2 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_2 == 0
    module_0.find_first_in_sorted(int_0, var_2)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "l[Ew;\\n#\x0bl#pOd7=\x0c"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    dict_0 = {var_0: var_0}
    module_0.find_first_in_sorted(str_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.find_first_in_sorted(dict_0, bool_0)
    assert var_0 == 0
    str_0 = "M"
    tuple_0 = (var_0, var_0)
    var_1 = module_0.find_first_in_sorted(tuple_0, var_0)
    assert var_1 == 0
    module_0.find_first_in_sorted(str_0, var_1)
