# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1671 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xcb%7n\x9d\xd8B\x12"
    list_0 = [bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "zlJ@xL25"
    set_0 = {str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 4
    module_0.func()
