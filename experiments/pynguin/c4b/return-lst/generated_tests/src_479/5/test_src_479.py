# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_479 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    bool_0 = True
    bool_1 = True
    tuple_0 = (dict_0, bool_0, bool_1)
    list_0 = [tuple_0, tuple_0, bool_1]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
