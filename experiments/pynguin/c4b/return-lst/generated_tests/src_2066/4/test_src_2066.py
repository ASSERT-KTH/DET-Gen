# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2066 as module_0


def test_case_0():
    bool_0 = True
    bool_1 = True
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_1, list_0, list_0]
    var_0 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"(i\xe0\xc2\x1b\xef\xc4\xdaMv\x8f\xc7"
    var_0 = module_0.func(*bytes_0)
    module_0.func()