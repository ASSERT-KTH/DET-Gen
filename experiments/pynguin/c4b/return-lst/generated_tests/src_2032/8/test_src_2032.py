# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2032 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "l"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1554.13991
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "H1eS\x0cbTt>KU"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    list_1 = [none_type_0, none_type_0]
    var_1 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xeb\xd6\xab0\x81AQ\xc9"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = []
    module_0.func(*list_1)
