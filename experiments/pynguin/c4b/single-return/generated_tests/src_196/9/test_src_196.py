# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_196 as module_0


def test_case_0():
    str_0 = "s/e+x"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "!"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "d]1!h<%ZS2by%f"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "DM)G'o}%!"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)