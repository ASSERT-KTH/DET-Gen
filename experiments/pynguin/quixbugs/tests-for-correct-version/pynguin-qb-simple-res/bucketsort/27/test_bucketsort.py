# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    bool_0 = True
    var_0 = module_0.bucketsort(list_0, bool_0)
    module_0.bucketsort(var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 2787
    str_0 = "\rN$)N!#@vZu1,"
    tuple_0 = (int_0, str_0)
    module_0.bucketsort(tuple_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "jDCzQyOa\x0c"
    module_0.bucketsort(str_0, str_0)