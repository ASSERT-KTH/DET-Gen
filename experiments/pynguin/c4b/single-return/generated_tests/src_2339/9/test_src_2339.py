# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2339 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "*W={O5=mN["
    bytes_0 = b"\x971\xa0f\xa2\xad\xde"
    tuple_0 = (str_0, bytes_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "W=HA{O5=mN["
    bytes_0 = b"\x971\xa0f\xa2\xad\xde"
    tuple_0 = (str_0, bytes_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "YES"
    module_0.func()
