# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "!)V;a\\!c}94<([?5:XzF"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1
    float_0 = 334.93367
    module_0.lis(float_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1a\x0f."
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 2
    module_0.lis(var_0)