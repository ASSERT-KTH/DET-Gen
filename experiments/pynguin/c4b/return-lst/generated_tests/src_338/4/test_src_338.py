# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_338 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"^\xc6\xac\x85mr\xb3%\xfc"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    tuple_0 = (set_0,)
    var_0 = module_0.func(*tuple_0)
    set_1 = set()
    module_0.func(*set_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa5\x15\xe8dj"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xa5\xe8d"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "y"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_1)
    module_0.func()