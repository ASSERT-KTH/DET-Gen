# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1371 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb9\xd6\xa7\xe5\x1cl\xd7*\x13\xa7\xaa\xd9\xab"
    list_0 = [bytes_0]
    module_0.func(*list_0)
