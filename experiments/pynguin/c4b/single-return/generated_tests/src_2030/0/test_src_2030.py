# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2030 as module_0
import builtins as module_1


def test_case_0():
    int_0 = 6311
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3155


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x06F\x82\xdcZn\xc9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    object_0 = module_1.object()
    module_1.object(*var_0, **var_0)
