# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2233 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "h8ello"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "h8elo"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "5hi(E0hX rp\x0cmEqGb"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, var_0, list_0, var_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "5hi(E0hX rp\x0cmEqGb"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "LQb Q~f`l>"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, var_0, list_0, var_0]
    module_0.func(*list_1)


def test_case_6():
    str_0 = "hello"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "JHSOlvb'S4-vz "
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = 'he"o'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "helloO"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)
    module_0.func()


def test_case_10():
    str_0 = "hellAL"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
