# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_223 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.func(*bool_0)


def test_case_1():
    str_0 = "UqoIe9Jx*"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
