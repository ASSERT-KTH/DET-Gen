# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2132 as module_0


def test_case_0():
    str_0 = "O#Yt<j*miZ8m&j+"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd0vv\xee\x99\xbb\xebJ\xc5|\xe1\x0f\xac"
    tuple_0 = (bytes_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"X\x1a\xd1\xd0i\xdfY36EXf\x10\x0e\xa1\xd1$\xaa\x0c"
    tuple_0 = (bytes_0,)
    list_0 = [bytes_0, bytes_0, tuple_0, bytes_0, tuple_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*tuple_0)
    assert var_1 == 1
    module_0.func()
