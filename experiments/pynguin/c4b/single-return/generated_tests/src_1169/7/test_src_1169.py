# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1169 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2389
    dict_0 = {int_0: int_0, int_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 2272466969
    int_1 = 546
    str_0 = "~7"
    tuple_0 = (int_1, str_0)
    list_0 = [tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()