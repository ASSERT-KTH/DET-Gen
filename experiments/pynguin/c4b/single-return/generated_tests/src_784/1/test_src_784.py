# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_784 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x03D"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"\x06=D"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
