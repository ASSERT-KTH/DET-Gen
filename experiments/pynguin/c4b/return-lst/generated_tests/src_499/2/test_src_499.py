# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_499 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x07\x0b\xa0\xe2_\x90&\xa9\xebN\xd8\xf10\xfdBs\xd0\xde"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "a\\"
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


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "$84CoL\nK\rO"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_4():
    str_0 = "h\\"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "K17Ux;\t$~H"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()


def test_case_6():
    str_0 = "a1"
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


def test_case_7():
    str_0 = "h1"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "h8"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)


def test_case_9():
    str_0 = "a8x_/)CZ"
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