# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2260 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb2"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Y94''(_ yX0sa(er9"
    list_0 = [str_0, str_0]
    module_0.func(*list_0)
