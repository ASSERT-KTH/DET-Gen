# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2134 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"M\xfbKK\xa4bX\xb9\xd1<v\x01z{"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x02\x0blD\x17\x7f\xb6\xd0.\x8aA_\xb4\x08\x1a!E\x95("
    module_0.func(*bytes_0)