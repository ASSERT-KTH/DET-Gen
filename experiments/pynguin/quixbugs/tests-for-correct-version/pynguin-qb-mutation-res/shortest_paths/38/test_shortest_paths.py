# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


def test_case_0():
    tuple_0 = ()
    var_0 = module_0.shortest_paths(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    module_0.shortest_paths(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3026
    module_0.shortest_paths(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(k"
    set_0 = {str_0, str_0}
    module_0.shortest_paths(str_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "&k"
    dict_0 = {str_0: str_0}
    module_0.shortest_paths(str_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "kk"
    dict_0 = {}
    var_0 = module_0.shortest_paths(str_0, dict_0)
    var_1 = module_0.shortest_paths(str_0, var_0)
    module_0.shortest_paths(var_0, var_1)