# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1761 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    bool_1 = True
    bool_2 = False
    int_0 = 2641
    tuple_0 = (bool_2, int_0)
    tuple_1 = (bool_1, tuple_0)
    bool_3 = True
    list_1 = [tuple_1, bool_1, bool_3]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bool_1 = False
    int_0 = 2641
    tuple_0 = (bool_1, int_0)
    tuple_1 = (bool_0, tuple_0)
    bool_2 = True
    var_0 = module_0.func(*tuple_1)
    list_0 = [tuple_1, bool_0, bool_2]
    module_0.func(*list_0)


def test_case_3():
    int_0 = 336
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.func(*dict_0)
