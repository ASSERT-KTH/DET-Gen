# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1107 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -503
    bytes_0 = b'e{\x13\xa5\x8c\x7f\xc6\x95\x14F"'
    list_0 = [int_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'e{\x13\xa5\x8c\x7f\xc6\x95\x14F"'
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x9c\x19+\x8d]\xbc\xef}N\x1bn\x97\xa6"
    list_0 = module_0.func(*bytes_0)
    module_0.func(*list_0)