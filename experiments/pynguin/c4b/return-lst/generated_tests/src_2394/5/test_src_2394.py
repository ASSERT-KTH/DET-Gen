# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2394 as module_0


def test_case_0():
    str_0 = "D3O\rvMIjjYDgU"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "D3O\rvN:jjjjjjXDg4"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, str_0, var_0, var_0, str_0, str_0, list_0]
    var_1 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "D3O\rvN:jjjjjjXDg4"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, var_0]
    var_1 = module_0.func(*list_1)
    none_type_0 = None
    list_2 = [list_1, str_0, var_1, var_1, none_type_0, str_0, list_1]
    var_2 = module_0.func(*list_2)
    var_3 = module_0.func(*list_2)
    module_0.func()
