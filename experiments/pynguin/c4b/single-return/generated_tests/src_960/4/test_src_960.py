# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_960 as module_0


def test_case_0():
    int_0 = 0
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x94f\x8b\xaa\x8dph\xfe*\xe6\x9c"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


def test_case_3():
    int_0 = 4
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xedn\x95M\xe6f'>\x98"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
