# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2309 as module_0


def test_case_0():
    str_0 = "0"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "0000000"
    set_0 = {str_0, str_0, str_0, str_0, str_0, str_0, str_0}
    list_0 = [str_0, set_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
