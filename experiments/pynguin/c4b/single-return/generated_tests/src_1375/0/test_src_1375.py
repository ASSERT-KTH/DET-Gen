# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1375 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b",\xcd.\xac\x7f\xc7\x02t\x84?!\xbe\x02r\xf5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Leonard"
    list_0 = []
    var_1 = module_0.func(*bytes_0)
    assert var_1 == "Leonard"
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x0c%\x00\x95\xd4\xd8p\x03"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Rajesh"
    module_0.func()