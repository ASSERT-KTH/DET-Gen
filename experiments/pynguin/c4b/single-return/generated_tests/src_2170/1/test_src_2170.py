# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2170 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    float_0 = -4181.106468
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 148079


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bytes_0 = b"a\xbe\xe9\xa6tZ\xf9D\xf3OHf\xfb\xd3u"
    tuple_0 = (bytes_0, bytes_0, bytes_0, bool_0)
    list_0 = [bool_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()
