# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1539 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b".\x80\x03\x94\x84\xdf\x14\xd6Q\xb1bs\x14t0\xeb\x9a\xd4\xd3"
    list_0 = [bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    set_0 = set()
    list_0 = [set_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "MV~K"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "fV~K"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()
