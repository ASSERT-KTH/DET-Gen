# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1043 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb4\xf1>R\xb0\xac\x1d\xebx\xa5`\r\x89\x95\xf4m"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Sheldon"
    module_0.func()
