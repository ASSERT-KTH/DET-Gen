# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1002 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "r}\\xt|ma\x0bly"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    set_0 = {bytes_0}
    module_0.func(*set_0)
