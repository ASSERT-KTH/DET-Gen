# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1869 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x0bow\x18\xae\xda\x99 \xe1)\xe4 \xb1\xa8"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 380.8809360938614
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -2828.86914
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_1.object()
    module_0.func()