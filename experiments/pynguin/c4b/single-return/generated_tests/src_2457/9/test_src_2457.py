# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2457 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x95\x1b\x92w\xb7\xa6\xdd\x17\x87\x9ee\x1fW_]%}\x10?\xd6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 9
    module_0.func()
