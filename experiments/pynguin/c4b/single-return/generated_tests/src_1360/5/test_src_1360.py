# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1360 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1017
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "444477777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777"
    )
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -877
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    module_1.object(*list_0, **var_0)
