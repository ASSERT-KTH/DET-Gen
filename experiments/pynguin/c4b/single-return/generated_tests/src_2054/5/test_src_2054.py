# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2054 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"+U\xd0*\x038b\x9c&\xe3V\xe5\xc4\xf2\xed"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 39
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xcb\x14\x83\xba\xb0<\xd9\x0c+\xad,\x80bo\x04\xb6\xa3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 199
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x82\xbd\x03\xdd"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 99
    module_0.func()
