# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1906 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "n}yC^a"
    list_0 = [str_0]
    list_1 = [str_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "nHyC^a"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*list_0)
    assert var_1 == "YES"
    module_0.func()
