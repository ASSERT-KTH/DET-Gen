# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1768 as module_0
import builtins as module_1


def test_case_0():
    str_0 = 'n\raO"'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 'n\raO"'
    var_1 = module_0.func(*list_0)
    assert var_1 == 'n\raO"'
    object_0 = module_1.object()
    var_2 = module_0.func(*str_0)
    assert var_2 == "N"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "2oS$et!:;z;t"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "2oS$et!:;z;t"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "n^O*H"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "N^o*h"
    object_0 = module_0.func(*var_0)
    assert object_0 == "n"
    var_1 = module_0.func(*list_0)
    assert var_1 == "N^o*h"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "O*H"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "o*h"
    module_1.object(*list_0, **var_0)
