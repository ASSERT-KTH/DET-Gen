# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_814 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    int_0 = 512
    bool_0 = True
    bytes_0 = b"=\x17\xd9"
    tuple_0 = (int_0, bool_0, int_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    assert (
        var_0
        == "44777777777777777777777777777777777777777777777777777777777777777777777777"
    )


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1"
    var_1 = module_0.func(*list_0)
    assert var_1 == "-1"
    list_1 = [var_0, list_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == "-1"
    module_0.func()