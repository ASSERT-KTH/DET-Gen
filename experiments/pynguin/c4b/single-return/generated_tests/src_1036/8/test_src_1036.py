# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1036 as module_0


def test_case_0():
    str_0 = "09001"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 901


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "090096791"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == 901058
    module_0.func()
