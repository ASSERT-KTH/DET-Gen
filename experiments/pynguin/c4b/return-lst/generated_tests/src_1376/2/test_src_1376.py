# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1376 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"Z\x17\xd3\xc4H\xbd\xe0!y\xdf\x00\xb8"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x8d\x17\xd3\xc4H\xbd\xe0!y\xdf\x00\xb8"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x88\x8b\x85V\xe0C\x0fR|\xf78:\xaei\xf1\xb7\xfa"
    var_0 = module_0.func(*bytes_0)
    list_0 = [var_0, bytes_0]
    module_0.func(*list_0)
