# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_338 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "87MxqSsu"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"O\xf6\x12\xc12\xd8\x03\xc6c\x89\x87\xb0\x12x\xfb\xac\xde\x05/j"
    bytes_1 = b"\xaf\x18\xac:"
    tuple_0 = (bool_0, bytes_0, bytes_1)
    list_0 = [tuple_0, bool_0, bytes_1]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "9g'T,)#4$Y}~"
    var_0 = module_0.func(*str_0)
    module_0.func()