# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2202 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x12\x1eZ\x9a\xf0"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa3\x9b\xec:\xdc\xca\x18"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x14 \xffG\xa8~\xa8\x109\xbf\xfd\x19}\x98U"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
