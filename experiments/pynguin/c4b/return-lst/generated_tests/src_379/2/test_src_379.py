# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_379 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x90\x14\xb3\xfc\x84\x81\xed\xaf"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
