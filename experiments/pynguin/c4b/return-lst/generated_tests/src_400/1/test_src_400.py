# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_400 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "+-1@]z"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Q-51"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "G|[8h9:!`}Ij#wz"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "2$,q{3S@DU8)\x0bAH+5"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
