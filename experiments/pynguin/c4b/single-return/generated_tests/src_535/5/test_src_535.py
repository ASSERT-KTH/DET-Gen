# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_535 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -544
    list_0 = [int_0, int_0, int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1737
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Leonard"
    bool_0 = True
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "Sheldon"
    var_2 = module_0.func(*list_1)
    assert var_2 == "Sheldon"
    module_0.func()
