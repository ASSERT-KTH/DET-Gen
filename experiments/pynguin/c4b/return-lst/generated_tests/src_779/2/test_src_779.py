# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_779 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9c\x95E\x8c\x90\xa1\xb9\xc3A\xf2v\x93i"
    var_0 = module_0.func(*bytes_0)
    module_1.object(**var_0)


def test_case_1():
    bytes_0 = b'\xe8\x99\x15\x87\x99 \x016"\xb2@p\xc4x \x9a \xa1`'
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x85\xdd\xaa"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x8f\x14\xcdNQ'\xa5\x1e\xc7"
    var_0 = module_0.func(*bytes_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 3482
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
