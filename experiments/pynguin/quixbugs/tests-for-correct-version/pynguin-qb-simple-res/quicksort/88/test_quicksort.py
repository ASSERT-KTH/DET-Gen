# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    module_0.quicksort(set_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    str_0 = "FD$.]m`\x0c|VVD\n>&B)]"
    tuple_0 = (bool_0, str_0)
    module_0.quicksort(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'bMB- !"_~PIpC o'
    var_0 = module_0.quicksort(str_0)
    var_1 = module_0.quicksort(str_0)
    var_2 = module_0.quicksort(str_0)
    int_0 = 855
    module_0.quicksort(int_0)