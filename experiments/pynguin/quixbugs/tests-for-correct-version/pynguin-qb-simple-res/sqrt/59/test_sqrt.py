# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


def test_case_0():
    int_0 = 1690
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(44.92348085373569, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    bool_1 = False
    var_1 = module_0.sqrt(bool_1, bool_1)
    assert var_1 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_2 = module_0.sqrt(var_1, bool_1)
    assert var_2 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_3 = module_0.sqrt(var_1, var_1)
    assert var_3 == pytest.approx(0.0, abs=0.01, rel=0.01)
    list_0 = []
    var_4 = module_0.sqrt(var_1, bool_1)
    assert var_4 == pytest.approx(0.0, abs=0.01, rel=0.01)
    module_0.sqrt(list_0, list_0)