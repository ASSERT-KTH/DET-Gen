# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1168 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"I\xb8\xaf\xb9\x0b0>\xa9N\x1d\x19\xc2d\xf2\xb1k\xdd#\x80\xbf"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2754
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"(B\xb4\xb4>g%"
    var_0 = module_0.func(*bytes_0)
    list_0 = [bytes_0]
    module_0.func(*list_0)
