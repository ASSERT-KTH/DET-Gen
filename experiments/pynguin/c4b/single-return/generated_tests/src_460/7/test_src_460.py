# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_460 as module_0


def test_case_0():
    bytes_0 = b"5r\xb6\x8c\x19=\x0f>L\x91\xef\xbb\xb3W\xb2\x0f\xbd\xdb"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)
