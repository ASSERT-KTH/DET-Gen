# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_463 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    bytes_0 = b"<'\xee+\x96\x15[\x99\x16;\x16\x1c\xf2>z\x19\xf4"
    list_0 = [bytes_0, none_type_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "@x"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "fO"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "@x"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "N"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)
