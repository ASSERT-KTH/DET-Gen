# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_894 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "VN9>4g4F>P3wA{rX"
    var_0 = module_0.func(*str_0)
    assert var_0 == "v"
    object_0 = module_1.object()
    module_1.object(*var_0)


def test_case_1():
    str_0 = "VN9>4g4F>P3wA{rX"
    var_0 = module_0.func(*str_0)
    assert var_0 == "v"
    object_0 = module_1.object()
    object_1 = module_0.func(*var_0)
    assert object_1 == "V"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Zu"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Zu"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "=p"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "=p"
    var_1 = module_1.object()
    var_2 = module_0.func(*var_0)
    assert var_2 == "="
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "lZ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Lz"
    var_1 = module_0.func(*list_0)
    assert var_1 == "Lz"
    object_0 = module_1.object()
    object_1 = module_1.object()
    var_2 = module_0.func(*var_1)
    assert var_2 == "l"
    var_3 = module_0.func(*var_2)
    assert var_3 == "L"
    module_0.func()
