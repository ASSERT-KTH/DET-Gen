# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1030 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"a\xb6_\x9b\xb2\xec\xef\xb86\x90\xca)+\x8a\xad=S"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)
