# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_593 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "%!D&_Tn\r\\px\x0ckm?3ad\\X"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "%!D&_Tn\r\\px\x0c9m?3ad\\X"
    bool_0 = False
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    bool_1 = False
    tuple_0 = (str_0, bool_0, var_1, bool_1)
    var_2 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "3hQJiF)w$"
    bool_0 = False
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)
    list_0 = [str_0, bool_0, var_1]
    var_2 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "H!T*&$"
    var_0 = module_0.func(*str_0)
    var_1 = module_1.object()
    module_0.func(*var_1)
