# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2238 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "e)"
    var_0 = module_0.func(*str_0)
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9)"
    var_0 = module_0.func(*str_0)
    none_type_0 = None
    module_0.func(*none_type_0)
