# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_388 as module_0


def test_case_0():
    str_0 = "a;ZRImRNg8t~1\\@<"
    int_0 = -1267
    list_0 = [int_0, str_0]
    list_1 = [str_0, list_0, int_0, int_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 12


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
