# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 4254
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    int_1 = 558
    var_1 = module_0.to_base(int_1, int_1)
    assert var_1 == "10"
    var_2 = var_1.__iter__()
    var_0.update(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.to_base(bool_0, bool_0)
    assert var_0 == ""
    var_1 = module_0.to_base(bool_0, bool_0)
    assert var_1 == ""
    module_0.to_base(var_1, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"7\x9f\xdd@\xd3.\x91\xf0\xb6\x9e\xa6b9&"
    module_0.to_base(bytes_0, bytes_0)