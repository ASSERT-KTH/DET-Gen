# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2030 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb2{ah\xb9v\x8a\x8c\xa5\xadgb\x08\xc3\xd7\xcf\xcc\xfc\xe5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 88
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
