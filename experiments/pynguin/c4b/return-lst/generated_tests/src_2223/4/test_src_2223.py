# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2223 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "/z4VqPRR+Z^dx>w\x0b="
    bool_0 = False
    bytes_0 = b"h\xf7J\xd1"
    tuple_0 = (bool_0, bytes_0)
    tuple_1 = (str_0, str_0, tuple_0, bool_0)
    list_0 = [tuple_1, bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = []
    list_1 = [list_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Q"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()
