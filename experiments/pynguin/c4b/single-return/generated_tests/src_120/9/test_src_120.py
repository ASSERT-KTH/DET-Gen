# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_120 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"ZK\xd4\x04y\x1c/4C\xb7\xfa\xcf"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "40032"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
