# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'p?\\W}Sw8vC9=*7"k!pP'
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.flatten(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "p?\\W;Sw8v&9=*7hk!pP"
    list_0 = [str_0, str_0]
    tuple_0 = (list_0,)
    var_0 = module_0.flatten(tuple_0)
    module_1.object(*var_0)