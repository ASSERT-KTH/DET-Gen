# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_964 as module_0


def test_case_0():
    bytes_0 = b'\xa58\x83\xfez\xb4"\xdc\x8cP\xa7'
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1546
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_4():
    bytes_0 = b'\xa58\x83\xfez\xb4"\xdc\x8cP\xa7'
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x97sdm\x05\xe5\xdfT"
    var_0 = module_0.func(*bytes_0)
    module_0.func()