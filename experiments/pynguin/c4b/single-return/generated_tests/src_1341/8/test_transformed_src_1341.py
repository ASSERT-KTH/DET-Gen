# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1341 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "1R"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_2():
    str_0 = "7r"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 16


def test_case_3():
    str_0 = "4R"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7


def test_case_4():
    str_0 = "1b"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "1a"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 4
    object_0 = module_0.func(*list_0)
    assert object_0 == 4
#    module_1.object(*var_0)


def test_case_6():
    str_0 = "6c"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == 29


def test_case_7():
    str_0 = "1d"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3


def test_case_8():
    str_0 = "2f"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8
    var_1 = module_0.func(*list_0)
    assert var_1 == 8


def test_case_9():
    str_0 = "1e"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
