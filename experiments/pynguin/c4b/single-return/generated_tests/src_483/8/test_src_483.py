# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_483 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "[("
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    tuple_0 = (bytes_0,)
    list_0 = [bytes_0, bytes_0, tuple_0, bytes_0]
    module_0.func(*list_0)
