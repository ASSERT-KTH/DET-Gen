# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_702 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x97)\xee\x9c*R{\xfc\x10\xba8\xfd\x16\xdc\x81\xb9\xd0~\xb2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 1
    module_0.func()