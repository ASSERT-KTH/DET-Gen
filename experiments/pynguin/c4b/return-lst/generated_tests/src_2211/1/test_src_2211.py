# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2211 as module_0


def test_case_0():
    bytes_0 = b"\xa8B\xe3\xc8\xeaz\xde P\xbd\xc7\x1fDWU\xec"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    int_0 = 2581
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "7(c~`U(>?e\t"
    var_0 = module_0.func(*str_0)
    module_0.func()
