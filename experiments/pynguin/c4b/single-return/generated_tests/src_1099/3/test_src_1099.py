# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1099 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1102
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "05:24"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 2207
    tuple_0 = (int_0, int_0, int_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "10:54"
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 4506
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "00:12"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 1142
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "06:04"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -404
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-4:20"
    module_1.object(*list_0)
