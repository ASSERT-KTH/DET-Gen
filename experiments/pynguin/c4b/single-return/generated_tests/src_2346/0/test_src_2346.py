# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2346 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".f.l.s"
    set_0 = {bool_0}
    list_1 = [set_0, bool_0, set_0, set_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == ".f.l.s"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
