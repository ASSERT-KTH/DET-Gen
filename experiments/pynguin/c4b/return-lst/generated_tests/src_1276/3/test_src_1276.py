# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1276 as module_0


def test_case_0():
    str_0 = "\x0bb#6,J~;jjldm9R\rc/["
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    tuple_0 = (bool_0, set_0)
    list_0 = [tuple_0, tuple_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "u/qYy3{~jVEDV\nQLT"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "\x0bbn6,J~;lJm9R\rc/="
    list_1 = [str_1, str_1, str_1, str_1]
    var_1 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "JfWvbH~wh|:!F9^"
    var_0 = module_0.func(*str_0)
    tuple_0 = (str_0,)
    var_1 = module_0.func(*tuple_0)
    module_0.func()
