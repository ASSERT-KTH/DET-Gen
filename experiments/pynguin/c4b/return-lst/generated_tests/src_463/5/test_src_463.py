# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_463 as module_0
import builtins as module_1


def test_case_0():
    str_0 = ";l|\x0c]&'Lb~iWA.hS8!"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xeb\x8a\x173\x1c+\x11h\x04\xe0\xe7\xb7A\x12\xe3tov\xe1\xaa"
    tuple_0 = (bytes_0, bytes_0)
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "U!G/U4Ou+x%8/CumV"
    var_0 = module_0.func(*str_0)
    object_0 = module_1.object()
    var_1 = module_1.object()
    list_0 = [str_0, str_0, object_0]
    var_2 = module_0.func(*list_0)
    module_0.func(*object_0)


def test_case_4():
    str_0 = "h5;D<O+"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)