# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.quicksort(bool_0)


def test_case_1():
    str_0 = ""
    tuple_0 = (str_0,)
    var_0 = module_0.quicksort(tuple_0)
    none_type_0 = None
    var_1 = module_0.quicksort(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)
    list_0 = [bool_0, bool_0, bool_0]
    var_1 = module_0.quicksort(list_0)
    module_0.quicksort(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "W5\rauEE[9"
    var_0 = module_0.quicksort(str_0)
    none_type_0 = None
    var_1 = module_0.quicksort(none_type_0)
    var_2 = module_0.quicksort(var_1)
    var_3 = module_0.quicksort(str_0)
    str_1 = "]@_7W)$JJ2;!]9:]j#,)"
    str_2 = "RD9v\r=[xL1L"
    dict_0 = {
        str_0: none_type_0,
        str_1: none_type_0,
        str_1: none_type_0,
        str_2: none_type_0,
    }
    module_1.object(**dict_0)