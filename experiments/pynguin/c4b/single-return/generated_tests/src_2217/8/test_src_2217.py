# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2217 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 37
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 4
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()