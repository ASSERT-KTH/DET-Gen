# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2258 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"A"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "i?OWa\r~BAOFLi%)9N\nc"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "i?OWa\r~BAOFLi%)9N\nc"
    set_0 = {str_0, str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "w\x0b\x0b"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "i?OWa\r~BAOFLi%)9N\nc"
    var_1 = module_0.func(*str_1)
    list_1 = [str_1, str_1]
    var_2 = module_0.func(*list_1)
    object_0 = module_1.object()
    module_0.func()
