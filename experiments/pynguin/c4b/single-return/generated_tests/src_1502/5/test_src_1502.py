# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1502 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 662
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "188 190"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 650
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "185 186"
    module_0.func()


def test_case_3():
    int_0 = 650
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "185 186"
    var_1 = module_0.func(*list_0)
    assert var_1 == "185 186"
    var_2 = module_0.func(*var_1)
    assert var_2 == "0 1"
    var_3 = module_0.func(*list_0)
    assert var_3 == "185 186"


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 665
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "190 190"
    module_0.func()
