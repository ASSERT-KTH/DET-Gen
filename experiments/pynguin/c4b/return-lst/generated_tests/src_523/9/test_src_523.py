# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_523 as module_0


def test_case_0():
    bytes_0 = b"\x9d\xaf<\xb1|`\xe6\xcc\x07\xd8"
    var_0 = module_0.func(*bytes_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    list_1 = []
    module_0.func(*list_1)
