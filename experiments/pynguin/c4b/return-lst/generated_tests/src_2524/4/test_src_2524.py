# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2524 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    list_1 = [set_0]
    list_2 = [set_0, list_0]
    var_1 = module_0.func(*list_2)
    var_2 = module_0.func(*list_1)
    module_0.func()


def test_case_1():
    str_0 = "Is2N?9"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
