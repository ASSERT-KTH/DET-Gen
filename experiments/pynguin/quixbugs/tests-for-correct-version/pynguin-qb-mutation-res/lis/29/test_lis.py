# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x8c\x92\x14\xbe\x9c"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 3
    module_0.lis(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.lis(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1
    bool_1 = False
    module_0.lis(bool_1)