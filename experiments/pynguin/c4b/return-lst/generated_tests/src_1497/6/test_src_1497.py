# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1497 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "_xSGh%[<a0"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    bytes_0 = b"!6I"
    complex_0 = -1091.9012 + 2172.9519578350933j
    list_0 = [bytes_0, complex_0, bytes_0, complex_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"j\x9cH\xaf\x90\x05\xc0\xcd\xb9\xb2(\x96Q"
    dict_0 = {}
    list_0 = [bytes_0, bytes_0, dict_0]
    module_0.func(*list_0)


def test_case_5():
    str_0 = "!\x0c"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "Q\x0c"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()
