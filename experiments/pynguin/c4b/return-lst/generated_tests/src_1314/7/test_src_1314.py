# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1314 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb5\x9c\xe8\xd6l\xb3("
    var_0 = module_0.func(*bytes_0)
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()