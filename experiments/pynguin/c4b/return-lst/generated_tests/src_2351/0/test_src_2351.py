# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2351 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x8cL\xf0\xaa\xb0\xf3\xc0\xde\xdd\x83p\x1d\x9c\x0b\xba\xf3%g"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1557
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"+\xbc\x08\x15J1\xde\xe0+\xae\x96o\x1cM\xa5"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
