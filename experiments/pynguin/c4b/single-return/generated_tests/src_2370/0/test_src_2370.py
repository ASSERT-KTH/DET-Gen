# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2370 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x12"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "IGNORE HIM!"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
    list_1 = [set_0, set_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "CHAT WITH HER!"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
