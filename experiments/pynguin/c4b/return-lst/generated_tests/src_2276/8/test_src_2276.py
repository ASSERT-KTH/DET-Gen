# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2276 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "n7#)HTV\r;$U8K80pu"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = ";"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "o),Nl=c)"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    list_1 = []
    list_2 = [list_1, list_1]
    list_3 = [list_2, list_2, list_2]
    module_0.func(*list_3)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "o),Nl=c)"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    bool_0 = True
    list_0 = [str_0, str_0, bool_0, bool_0]
    var_2 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "o),N=)"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    list_0 = [str_0, str_0, var_0, var_0]
    var_2 = module_0.func(*list_0)
    module_1.object(**var_2)
