# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1923 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Ip\x0cFs:cf"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "2\n4"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "ab"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9\n4"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "abcdabcda"
    module_1.object(*var_0)
