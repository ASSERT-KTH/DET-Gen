# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1761 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x17\xff\x08=sP\x1b\xf6*\xd1\xba\xa5\x9c"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()