# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1696 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa0\x87\xecK,\x85~\x9dUi\xc4;\xe4\xfc\xb5:K\t\xb5"
    int_0 = 156
    list_0 = [bytes_0, int_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 252
    module_0.func(*bytes_0)
