# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_712 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"y\xf4\x01\xdf]dn\x9fY\x02\x83\x13\xb8\x14\x97\x08"
    int_0 = -863
    object_0 = module_0.object()
    list_0 = [int_0, bytes_0, bytes_0, object_0]
    var_0 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa0\x1c \xe3{\xf7\x94\ng]X\xce["
    module_1.func(*bytes_0)
