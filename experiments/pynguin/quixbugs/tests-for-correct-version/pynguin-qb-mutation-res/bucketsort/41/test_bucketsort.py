# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    str_0 = "\t 4f}Gx`u[*(\r5@s,0I"
    tuple_0 = (bool_0, bool_0, str_0)
    int_0 = 1203
    module_0.bucketsort(tuple_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.bucketsort(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    tuple_0 = (bool_0, bool_0, bool_0)
    int_0 = 1203
    var_0 = module_0.bucketsort(tuple_0, int_0)
    module_0.bucketsort(var_0, var_0)