# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1269 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = False
    bytes_0 = b"/\x1c\xf9b\xb6\x8c\xfc\x9f\xde\x1bK\xef"
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"/\x1c\xf9b\xb6\x8c\xfc\x9f\xde\x1bK\xef"
    list_0 = [bool_0, bytes_0]
    module_0.func(*list_0)


def test_case_3():
    str_0 = "9"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "9"
    float_0 = 656.1075
    list_0 = [float_0, str_0]
    module_0.func(*list_0)
