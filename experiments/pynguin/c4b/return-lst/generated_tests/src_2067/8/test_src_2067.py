# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2067 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x14\x90\xbd\xc0\xff 1y>~\xd0ZU\x10\xc9\x97\xa8S\xd4"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\x14\x90\xbd\xc0\xff\xf3\x8a1y>~\xd0ZU\x10\xc9\x97\xa8S\xd4"
    var_1 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 254
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x02g4Y\x9a\xd7\xd9\xfd\x13X\xa0"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)
