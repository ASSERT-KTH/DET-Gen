# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1795 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "stXNjM9hazQ]11rEI\x0b"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "stXNjM9hazQ]11rEI\x0b"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 16


def test_case_3():
    str_0 = "stXRNjM9hazQ]1rUI\x0b"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 16


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ":O],_>kd0q45i"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 12
    module_1.object(*list_0, **list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "M3<A030\x0cVnoCp:vn"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 13
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "YZXNjM9hae]\n1rEI\x0b"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 14
    module_0.func(*var_0)
