# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2350 as module_0


def test_case_0():
    str_0 = "^o1MS@a#u"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    bool_0 = True
    list_0 = [none_type_0, bool_0]
    var_0 = module_0.func(*list_0)
    str_0 = ")3?"
    bool_1 = True
    int_0 = 1940
    tuple_0 = (bool_0, str_0, bool_1, int_0)
    set_0 = {none_type_0, bool_1}
    dict_0 = {none_type_0: none_type_0, tuple_0: set_0, tuple_0: str_0}
    list_1 = [dict_0, bool_1, set_0]
    var_1 = module_0.func(*list_1)
    list_2 = [none_type_0, none_type_0]
    var_2 = module_0.func(*list_2)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.func(*list_0)
