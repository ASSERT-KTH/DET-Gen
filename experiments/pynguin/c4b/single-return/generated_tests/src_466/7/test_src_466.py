# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_466 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "1"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "3"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)
