# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1895
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(48.37853439619036, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(var_0, int_0)
    assert var_1 == pytest.approx(24.18926719809518, abs=0.01, rel=0.01)
    bool_0 = False
    var_2 = module_0.sqrt(bool_0, var_0)
    none_type_0 = None
#    module_0.sqrt(bool_0, none_type_0)


def test_case_1():
    bool_0 = True
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.5, abs=0.01, rel=0.01)
