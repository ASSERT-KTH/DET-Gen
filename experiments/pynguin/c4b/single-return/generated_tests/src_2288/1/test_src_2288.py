# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2288 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x1av"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "HSuW@::>H!hp#\x0bW\x0b1yQm"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".h.s.w.@.:.:.>.h.!.h.p.#.\x0b.w.\x0b.1.q.m"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
