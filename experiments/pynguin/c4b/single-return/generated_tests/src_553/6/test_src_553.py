# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_553 as module_0


def test_case_0():
    bytes_0 = b"\nc\x1f\xb6\xa4\xc6\x17\xd1"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 9


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    bool_0 = False
    list_0 = [dict_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "M;O"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    module_0.func()
