# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


def test_case_0():
    float_0 = 217.123703
    var_0 = module_0.sqrt(float_0, float_0)
    assert var_0 == pytest.approx(18.46924139152548, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.5, abs=0.01, rel=0.01)
    str_0 = "o9nyLu[r"
    module_0.sqrt(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.sqrt(list_0, list_0)