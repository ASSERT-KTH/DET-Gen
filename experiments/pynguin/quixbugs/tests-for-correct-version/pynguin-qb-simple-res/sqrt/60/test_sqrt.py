# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 501.559
    var_0 = module_0.sqrt(float_0, float_0)
    assert var_0 == pytest.approx(25.10107343091736, abs=0.01, rel=0.01)
    none_type_0 = None
    module_0.sqrt(float_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    list_0 = [bool_0, bool_0, bool_0]
    module_0.sqrt(list_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x01\xd1\xfb\x80L\xef\x00w\xcf"
    module_0.sqrt(bytes_0, bytes_0)