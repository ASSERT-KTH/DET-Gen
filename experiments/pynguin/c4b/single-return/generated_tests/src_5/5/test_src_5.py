# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_5 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = '74\rG,)*c?z{4#p"/`&p'
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    var_1 = module_0.func(*str_0)
    assert var_1 == 2
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "6m?rU2\\O9\r!oIB"
    var_0 = module_0.func(*str_0)
    assert var_0 == 4
    object_0 = module_1.object()
    var_1 = module_1.object()
    module_0.func(*object_0)
