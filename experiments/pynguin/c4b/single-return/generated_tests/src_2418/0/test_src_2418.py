# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2418 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    bytes_0 = b"\xc4\xbe\xdei"
    tuple_0 = (bytes_0, bytes_0)
    tuple_1 = (str_0, tuple_0, bytes_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "!e"
    bytes_0 = b"\xc4\xbe\xdei"
    tuple_0 = (bytes_0, bytes_0)
    tuple_1 = (str_0, tuple_0, bytes_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == "!e"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '}~L9&cl+j"R'
    bytes_0 = b"\xc4\xbe\xdei"
    tuple_0 = (bytes_0, bytes_0)
    tuple_1 = (str_0, tuple_0, bytes_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == '}~L9&cl+j"R'
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ");KMR^"
    bytes_0 = b"\xc4\xbe\xdei"
    tuple_0 = (bytes_0, bytes_0)
    tuple_1 = (str_0, tuple_0, bytes_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == ");kmr^"
    module_0.func()
