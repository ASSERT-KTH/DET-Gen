# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2132 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "3.,4Vp#I%\t"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    set_0 = {str_0, var_0, str_0}
    list_0 = [set_0, set_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"`\x9f\x01S7\xbd\x83\x7f\x9e\xf5\x98\xad0[\x7f\xb8}k"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"`\x9f\x01S7\xbd\x83\x7f\xf5\x98\x7f0[\x7f\xb8}k"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    object_0 = module_1.object()
    module_0.func(*bytes_0)
