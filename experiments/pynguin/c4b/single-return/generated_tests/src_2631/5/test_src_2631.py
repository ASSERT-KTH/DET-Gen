# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2631 as module_0


def test_case_0():
    int_0 = -3796
    str_0 = '@*z""axLx`\rGbFt'
    list_0 = [int_0, int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    var_1 = module_0.func(*list_0)
    assert var_1 == "7"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    bytes_0 = b"U\xa9\xf8\x1c\xd3\xbf\x0c\x1a9K\xd2O\xd5"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == "711111111111111111111111111111111111111111"
    var_2 = module_0.func(*list_0)
    assert var_2 == ""
    module_0.func()
