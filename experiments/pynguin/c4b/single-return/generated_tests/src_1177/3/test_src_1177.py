# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1177 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    list_1 = module_0.func(*var_0)
    assert list_1 == "711"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 186
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
    bytes_0 = b"4\xaf\x16\x9c\xc9N\x8d\xa8\xe7\x1d\xc65\xfc"
    list_1 = [bytes_0, bytes_0]
    module_0.func(*list_1)
