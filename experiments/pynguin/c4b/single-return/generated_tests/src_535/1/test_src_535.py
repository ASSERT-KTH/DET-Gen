# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_535 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"F(l\r"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Howard"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2901
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    module_0.func(*list_0)
