# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_487 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"T\xbb"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"."
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "%?aq0I0\\:6yN)o"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "fV[, "
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "wp$E\x0b"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*var_0)