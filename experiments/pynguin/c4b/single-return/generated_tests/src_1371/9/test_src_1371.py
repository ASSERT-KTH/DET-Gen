# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1371 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb6\x10\x9cU\xb6\xc3DoFo"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)
