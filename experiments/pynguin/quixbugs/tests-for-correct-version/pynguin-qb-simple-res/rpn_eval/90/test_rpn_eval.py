# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"a\x96k\xf1\x8f\xee\x01\xbf;dW5~"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.rpn_eval(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1745.2
    bool_0 = True
    bool_1 = False
    dict_0 = {float_0: bool_0, bool_0: float_0, bool_1: bool_0, bool_1: float_0}
    int_0 = 2501
    tuple_0 = (float_0, float_0, dict_0, int_0)
    module_0.rpn_eval(tuple_0)