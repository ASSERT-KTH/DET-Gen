# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_466 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1148
    str_0 = "T=\x0cEm.Ar3yq/"
    list_0 = [int_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1152
    str_0 = "A:Xr\n&H[@1"
    list_0 = [int_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1579
    str_0 = "=\x0cEm.Ar3yq/"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
