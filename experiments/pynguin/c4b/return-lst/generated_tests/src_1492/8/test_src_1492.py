# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1492 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "lNFQZ'"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "lNFQZ'"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)


def test_case_3():
    str_0 = "hello"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "eello"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x80W\xaf\xa7\xf1\xde\xcd\\\xf0s}U\xb2"
    str_0 = "helloo"
    list_0 = [str_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "hollo"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()
