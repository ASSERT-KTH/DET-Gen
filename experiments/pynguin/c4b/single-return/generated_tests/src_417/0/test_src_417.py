# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_417 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x96\xe2\xb1"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    tuple_0 = (dict_0,)
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, tuple_0, bytes_0]
    module_0.func(*list_0)