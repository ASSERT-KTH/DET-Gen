# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_557 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xc8\x98R["
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "it;LOmx*aEE9<"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Ri ;Q=Ib>^,{P"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_1.object()
    var_2 = module_0.func(*var_0)
    assert var_2 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "ir]HOms*EG9<"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()
