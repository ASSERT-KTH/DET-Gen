# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_483 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"N07's\n\x89o\xc3\x8b\x9e\xa6)\xf3\x93\xb9\xc1\x1aW"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)