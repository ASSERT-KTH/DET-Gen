# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_948 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xe7z\xc3E~r"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
