# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1387 as module_0
import builtins as module_1


def test_case_0():
    int_0 = -316
    dict_0 = {int_0: int_0}
    tuple_0 = (int_0, int_0, dict_0)
    list_0 = [tuple_0, dict_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    list_1 = [var_0, dict_0, var_0, list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"


def test_case_1():
    str_0 = "Sby9z*&2v6q n"
    set_0 = set()
    bool_0 = True
    list_0 = [str_0, set_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    object_0 = module_1.object()
    list_0 = [object_0, object_0]
    list_1 = [list_0]
    list_2 = [list_0, list_1, object_0, list_1]
    var_0 = module_0.func(*list_2)
    assert var_0 == "NO"
    module_0.func()
