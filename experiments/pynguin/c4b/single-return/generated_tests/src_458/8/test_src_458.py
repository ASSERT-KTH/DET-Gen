# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_458 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1250
    list_0 = []
    bool_0 = True
    dict_0 = {int_0: list_0, int_0: int_0, bool_0: bool_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 325521875
    module_0.func()


def test_case_1():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    list_0 = [bool_0, bool_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.func(*list_0)
