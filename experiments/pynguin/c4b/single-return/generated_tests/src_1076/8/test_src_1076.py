# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1076 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    str_0 = "9 9"
    list_0 = [str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 6270
    var_1 = module_0.func(*list_0)
    assert var_1 == 6270
    module_0.func()
