# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1585 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2408
    list_0 = [int_0, int_0, int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"a\xff\x9a\x1e\x08<\xd4_\x06(\x19\xe5"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa7\x05Z<\xed~\xd5\xa7:\xde\xc2\xd8v5"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)
