# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_403 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xffr\xe4\x03\xb3\xae\\\xc0\xe5i\xeb"
    list_0 = [bytes_0]
    list_1 = [list_0, bytes_0, list_0]
    var_0 = module_0.func(*bytes_0)
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x16\r\x06~\xb4:\xb9VA"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
