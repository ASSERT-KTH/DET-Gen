# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2230 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xdb"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


def test_case_2():
    str_0 = "jgc9&p xMO j%pC|"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "YES"
