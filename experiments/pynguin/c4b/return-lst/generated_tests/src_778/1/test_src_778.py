# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_778 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"Q \xf1N\x14\xa7\x01\xc4"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "7c2"
    module_0.func(*str_0)
