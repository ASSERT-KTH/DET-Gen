# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_460 as module_0
import builtins as module_1


def test_case_0():
    str_0 = 'oj"L*{E{r\\%F'
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -3295.0
    str_0 = "h)l1Bcx"
    bool_0 = True
    tuple_0 = (bool_0,)
    tuple_1 = (str_0, float_0, tuple_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == "NO"
    set_0 = {float_0}
    list_0 = [set_0, set_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"
    var_2 = module_1.object()
    module_0.func()