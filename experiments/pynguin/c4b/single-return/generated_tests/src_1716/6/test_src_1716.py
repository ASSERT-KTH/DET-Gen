# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1716 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "sL09CnhYo W*T=D<W\x0c@"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)
