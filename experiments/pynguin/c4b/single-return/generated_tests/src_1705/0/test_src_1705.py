# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1705 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"% \x019\xa4uL5W\xe3\xbd\x0f\x96\x8c4\xcd\xd4\x95"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb5\xb5'_\xf2\xf4\xd0\xaey\xde\x1cz\xf8hW\x14\x8d"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 39
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


def test_case_4():
    bytes_0 = b"?q\x00\x8bJA\xd2\xc5\x94\tV\x18\x17E\x99\xe2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 63
