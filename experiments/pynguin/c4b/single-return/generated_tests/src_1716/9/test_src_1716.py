# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1716 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xf8P\n \xf5\x1d\rE\x8f\xae\xfd\xe6\xa0"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\ndx5Dxq"
    module_0.func(*str_0)
