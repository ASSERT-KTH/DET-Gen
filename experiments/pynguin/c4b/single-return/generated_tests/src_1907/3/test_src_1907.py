# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1907 as module_0


def test_case_0():
    str_0 = "e9-&\x0c3"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 3233.264
    module_0.func(*float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "c!b:X0.WW[~$ugs6G"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "W%S@\t^MGvp0SgBB'4U"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()
