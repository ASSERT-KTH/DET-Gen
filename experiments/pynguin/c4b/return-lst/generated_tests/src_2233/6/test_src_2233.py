# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2233 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "l"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "l"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)


def test_case_3():
    str_0 = "e"
    var_0 = module_0.func(*str_0)


def test_case_4():
    str_0 = "`JBOl$\n''Ou08vH6^"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "hellH"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "Z4c\x0bpH )Wl L"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_7():
    str_0 = "hello"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_8():
    str_0 = "hWeQio"
    list_0 = [str_0]
    object_0 = module_0.func(*list_0)
    var_0 = module_1.object()
    var_1 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "heElo"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "hllo"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*list_0, **str_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = "hellL1o"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_12():
    str_0 = "hellLOo"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()
