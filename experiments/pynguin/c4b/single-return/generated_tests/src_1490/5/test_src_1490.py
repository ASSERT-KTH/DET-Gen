# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1490 as module_0


def test_case_0():
    str_0 = "ruV7O$9"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "i):.Cl,Bie M"
    list_0 = [str_0, str_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"m\xab"
    module_0.func(*bytes_0)
