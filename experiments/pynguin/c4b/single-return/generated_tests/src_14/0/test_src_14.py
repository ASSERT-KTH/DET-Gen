# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_14 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = [var_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x16`V\xd8f_\x14\x91>\xaa"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()
