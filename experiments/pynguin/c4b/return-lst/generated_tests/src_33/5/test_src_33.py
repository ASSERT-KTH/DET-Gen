# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_33 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"Op\xa90\xfd\xcd\xcdm\xb6\xa5f \xe7o\x08&"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    module_0.func(*list_0)
