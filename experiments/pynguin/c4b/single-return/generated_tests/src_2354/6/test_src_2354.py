# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2354 as module_0


def test_case_0():
    str_0 = "c+A`=3Pa}V*l^"
    float_0 = -3900.0
    tuple_0 = (str_0, float_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".c.+.`.=.3.p.}.v.*.l.^"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ""
    float_0 = 490.3666
    list_0 = [str_0, float_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()
