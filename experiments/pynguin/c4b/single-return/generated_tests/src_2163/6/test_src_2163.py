# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2163 as module_0


def test_case_0():
    set_0 = set()
    list_0 = [set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'W"\xce\xc7c\x9e^\x0f\x19'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 2
    module_0.func(*var_0)
