# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2631 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, var_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    list_1 = [none_type_0, none_type_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    list_1 = module_0.func(*var_0)
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)
    list_2 = []
    module_0.func(*list_2)
