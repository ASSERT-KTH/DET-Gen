# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2267 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -50.7
    dict_0 = {float_0: float_0}
    list_0 = [dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "i;C:[Xi}TJHT"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "nD["
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    var_2 = module_0.func(*list_0)
    module_0.func()
