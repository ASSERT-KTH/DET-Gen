# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2094 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"m\xcc\x15\xed\x0bN"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xec\xde\x90\xad\xc1V\n\xbdE"
    str_0 = "k[ed;{AXerE{"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".k.[.d.;.{.x.r.{"
    list_1 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_1)
