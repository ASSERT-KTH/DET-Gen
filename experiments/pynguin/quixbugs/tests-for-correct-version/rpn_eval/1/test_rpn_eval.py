# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\n-1#e\ni"
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    module_0.rpn_eval(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.rpn_eval(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -1172.345
    int_0 = -2252
    tuple_0 = (float_0, float_0, float_0, int_0)
    module_0.rpn_eval(tuple_0)
