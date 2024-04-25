# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0
import builtins as module_1


def test_case_0():
    set_0 = set()
    var_0 = module_0.find_in_sorted(set_0, set_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 4384
    dict_0 = {int_0: int_0}
    module_0.find_in_sorted(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.find_in_sorted(list_1, list_0)
    assert var_0 == 0
    bytes_0 = b"\x08\xba\x7f"
    none_type_0 = None
    module_0.find_in_sorted(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    float_0 = -599.4042
    str_0 = "6cu9}%"
    str_1 = "R"
    var_0 = module_0.find_in_sorted(str_0, str_1)
    assert var_0 == -1
    dict_0 = {str_0: str_0, str_1: bool_0, str_0: float_0, str_1: float_0}
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "{cu9"
    str_1 = "R"
    var_0 = module_0.find_in_sorted(str_0, str_1)
    assert var_0 == -1
    module_0.find_in_sorted(var_0, str_1)