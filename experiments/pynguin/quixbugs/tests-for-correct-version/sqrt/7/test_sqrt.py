# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


def test_case_0():
    bool_0 = True
    bool_1 = True
    var_0 = module_0.sqrt(bool_0, bool_1)
    assert var_0 == pytest.approx(0.5, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Rq>}nrt@D+"
    module_0.sqrt(str_0, str_0)


def test_case_2():
    int_0 = 625
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(29.164261314427797, abs=0.01, rel=0.01)
