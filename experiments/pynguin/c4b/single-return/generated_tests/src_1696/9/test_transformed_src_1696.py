# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1696 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1093.0733
    tuple_0 = (float_0,)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == pytest.approx(-1093.0733, abs=0.01, rel=0.01)
#    module_0.func()
