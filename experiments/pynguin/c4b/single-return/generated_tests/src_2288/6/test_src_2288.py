# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2288 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0, bool_0, bool_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "V-o'n9h\x0c"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".v.-.'.n.9.h.\x0c"
    module_0.func()
