# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2425 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x84\x9b]\xb7\xae\x1f\xb7\x84\xca\x9e\x8b\x0c#"
    var_0 = module_0.func(*bytes_0)
    module_0.func()