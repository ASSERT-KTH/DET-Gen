# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_152 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -282.1146
    bytes_0 = b"\x0bP@\xa0\xc3+F\xdaWlEh\xdf!\x94\xe1\x1ed-"
    complex_0 = 737 + 652.9j
    tuple_0 = ()
    dict_0 = {complex_0: float_0, tuple_0: tuple_0, bytes_0: bytes_0, tuple_0: float_0}
    list_0 = [float_0, bytes_0, complex_0, dict_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x0bP@\xa0\xc3+F\xdaW\xceEh\xdf!\x94\xe1\x1ed-"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ":-FD"
    bool_0 = False
    int_0 = -2043
    list_0 = [int_0, str_0]
    list_1 = [bool_0, int_0, list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_1)
    module_0.func()