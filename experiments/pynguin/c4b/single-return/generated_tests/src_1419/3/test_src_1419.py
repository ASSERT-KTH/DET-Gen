# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1419 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ".5O0Z"
    var_0 = module_0.func(*str_0)
    assert var_0 == "."
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "#0_T^1PdK="
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "#0_T^1PdK="
    list_1 = [str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "#0_T^1PdK="
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "z6E4,%\x0bQD"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Z"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "s\n;W/cb7?\x0c Vf\x0b_z-\\"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "s;W/cb7?Vf_z-\\"
    str_1 = "z6E4,%\x0bQD"
    var_1 = module_0.func(*str_1)
    assert var_1 == "Z"
    object_0 = module_1.object()
    module_0.func(*object_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "u5{0Z"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "U5{0z"
    var_1 = module_0.func(*str_0)
    assert var_1 == "U"
    module_0.func()