# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1634 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"N\x7fQ 3\xf4\xcc\x19\xfay7@\xf4\xaeg;\x95;/\xc8"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0|wF"
    module_0.func(*str_0)
