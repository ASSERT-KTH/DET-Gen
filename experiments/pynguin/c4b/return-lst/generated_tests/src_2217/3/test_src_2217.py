# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2217 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"!\xd8\xd7!\x80\xe0\xae"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3902
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"@\xd8\xd71\x80\xe0\xae"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x07\xcbN\xa8\x15R\x91\xbb"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)