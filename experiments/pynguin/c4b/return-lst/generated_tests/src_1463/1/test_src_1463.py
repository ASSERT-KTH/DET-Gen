# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1463 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "O\\Wa|h^lQ"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "O\\WA|H^LQ"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "mJ0a"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "v"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)