# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_768 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"z\xed\x07"
    module_0.func(*bytes_0)
