# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1666 as module_0


def test_case_0():
    str_0 = "~MiL\ro"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "H%VV]SdNx"
    bytes_0 = b"\xa9\xbaP\x0cX\xc7\xea\xe3O"
    list_0 = [str_0, str_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0


def test_case_3():
    str_0 = "10yrc@lKK="
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
