# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1604 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "s\nZD 2?m\\`B\x0c*OA"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "4hsn@1j|"
    int_0 = 4270
    set_0 = {int_0, int_0, int_0}
    list_0 = [str_0, str_0, str_0, set_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*list_0, **str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
