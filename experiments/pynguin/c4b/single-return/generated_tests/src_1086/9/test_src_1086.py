# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1086 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -591
    bytes_0 = b"\xb11\x19"
    set_0 = {int_0, bytes_0, int_0, bytes_0}
    list_0 = [int_0, int_0, set_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()
