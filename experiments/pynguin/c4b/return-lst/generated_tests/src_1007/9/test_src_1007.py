# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1007 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "tQkE1"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0{"
    var_0 = module_0.func(*str_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '4su\n#t\r"'
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "5QR"
    var_0 = module_0.func(*str_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "3hg"
    bool_0 = False
    var_0 = module_0.func(*str_0)
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "1"
    var_0 = module_0.func(*str_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "2W"
    var_0 = module_0.func(*str_0)
    object_0 = module_1.object()
    module_0.func(*var_0)
