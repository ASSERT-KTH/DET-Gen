# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2459 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x11{`\xecXm\xcb"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x11{`Xm"
    var_0 = module_0.func(*bytes_0)
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x11`\xdcXm\xcb"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
