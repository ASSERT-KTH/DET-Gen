# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2288 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 653
    set_0 = {int_0, int_0, int_0, int_0}
    list_0 = [set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [dict_0, tuple_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "xAZWo"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
