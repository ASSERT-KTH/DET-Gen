# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1769 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "zyB&=q"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "zyb&=q"


def test_case_1():
    str_0 = "6+&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "6+&"
    object_0 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1002
    module_0.func(*int_0)
