# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1769 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1938
    set_0 = {int_0, int_0, int_0, int_0}
    list_0 = [set_0, set_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "B\r?)W@R_-?1i{[\n`2E^/"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "}Cs}a)pmhwH\n"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()