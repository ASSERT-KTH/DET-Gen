# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2377 as module_0


def test_case_0():
    str_0 = "/!rqO-$Nb^n?:H@"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "<-jn\tYOh//m!"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = 'h\x0b"7\tr!9</l\rW[Jne'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = 'h\x0b"7\tr!e9</l\rW[Jne'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "h\x0b7\t!e9</l\r[lJne"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "h\x0b7\t!e9</l\r[loJne"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)
