# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 406
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(21.88572483174967, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(int_0, var_0)
    assert var_1 == pytest.approx(20.218314865386922, abs=0.01, rel=0.01)
    bool_0 = False
    var_2 = module_0.sqrt(bool_0, var_0)
    assert var_2 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_3 = module_0.sqrt(var_1, var_1)
    assert var_3 == pytest.approx(6.054578716346731, abs=0.01, rel=0.01)
    var_4 = module_0.sqrt(bool_0, bool_0)
    assert var_4 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_5 = module_0.sqrt(bool_0, bool_0)
    assert var_5 == pytest.approx(0.0, abs=0.01, rel=0.01)
    object_0 = module_1.object()
    module_0.sqrt(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    none_type_0 = None
    module_0.sqrt(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.sqrt(none_type_0, none_type_0)