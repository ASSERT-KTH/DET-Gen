# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_466 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "1"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\r\xd9\x14\xdb\xedI"
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "00"
    module_0.func()
