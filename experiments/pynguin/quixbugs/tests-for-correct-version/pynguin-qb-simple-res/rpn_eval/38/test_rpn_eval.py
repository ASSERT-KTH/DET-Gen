# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xf7\x17\xa5\xab\x15v\xc3B\x03\xcf\x18\xebC1\xce"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.rpn_eval(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -2426.566335 - 528.38j
    module_0.rpn_eval(complex_0)


def test_case_3():
    float_0 = -4064.45
    set_0 = {float_0}
    var_0 = module_0.rpn_eval(set_0)
    assert var_0 == pytest.approx(-4064.45, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -19.8
    complex_0 = 597.4 + 3832.0128j
    tuple_0 = (float_0, float_0, float_0, complex_0)
    module_0.rpn_eval(tuple_0)