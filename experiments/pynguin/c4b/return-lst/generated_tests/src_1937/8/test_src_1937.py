# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1937 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "KZ"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, var_0]
    var_1 = module_0.func(*list_0)
    module_1.object(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "RG"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "bF?v8"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "bF?"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, var_0]
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "?J"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)
    object_0 = module_1.object()
    module_1.object(**var_2)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "aZ"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, var_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*str_0)
    var_3 = module_1.object()
    module_0.func()
