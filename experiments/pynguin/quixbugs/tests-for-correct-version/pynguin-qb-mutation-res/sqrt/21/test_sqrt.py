# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 762
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(33.60424607582555, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(int_0, int_0)
    assert var_1 == pytest.approx(33.60424607582555, abs=0.01, rel=0.01)
    bool_0 = False
    var_2 = module_0.sqrt(bool_0, bool_0)
    assert var_2 == pytest.approx(0.0, abs=0.01, rel=0.01)
    bool_1 = False
    var_3 = module_0.sqrt(bool_0, bool_1)
    var_4 = module_0.sqrt(bool_1, var_3)
    list_0 = [bool_0, bool_0]
    module_0.sqrt(list_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    module_0.sqrt(tuple_0, tuple_0)