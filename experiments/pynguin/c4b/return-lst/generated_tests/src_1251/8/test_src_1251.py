# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1251 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    list_0 = [dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    str_0 = "XR-N,n"
    list_0 = [object_0, object_0, str_0, object_0]
    list_1 = [list_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "&Cl@wd\n75R:X9F+X"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "&Cl@wd\n75R:X9F}X"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
