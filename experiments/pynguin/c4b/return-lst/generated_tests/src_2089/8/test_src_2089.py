# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2089 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x9d\xba\x11\xcf\xa1g\xe8~@\xa7(\x1f\x00\xe3\xb6\x15\xc9\xfc"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"\xe3"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    bytes_0 = b"\x82Zt\xfbMq\xb2+\x9e\x9e\xaaQZ\x15\xc9\x18\xd5a\x9c"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -252
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    list_1 = [list_0, list_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    list_2 = [var_0, var_0, list_0]
    module_1.object(*list_2, **var_0)
