# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2245 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "b\nOkpuwnIIn:"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "b\nOkpuwnIIn:"


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "b\nOkpuwnIIn:"
    var_0 = module_0.func(*str_0)
    assert var_0 == "B"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\nOkpuwnIIn:"
    var_0 = module_0.func(*str_0)
    assert var_0 == "\n"
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "K@ftz!"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == "k"
    var_1 = module_0.func(*list_0)
    assert var_1 == "K@ftz!"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "JcOkpunIn:"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "JcOkpunIn:"
    var_1 = module_1.object()
    module_0.func()
