# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1749 as module_0


def test_case_0():
    float_0 = -28.121
    set_0 = {float_0, float_0, float_0}
    tuple_0 = (float_0, set_0)
    var_0 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe7\xc1\xf1"
    var_0 = module_0.func(*bytes_0)
    module_0.func()