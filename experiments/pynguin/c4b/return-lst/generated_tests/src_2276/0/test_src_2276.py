# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2276 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "S\n&5*=Zub2MVd[p5r"
    var_0 = module_0.func(*str_0)
    object_0 = module_1.object()
    str_1 = "p7waJww\x0c5NGvYDs\nBt5\r"
    list_0 = [str_1, str_0, str_1]
    var_1 = module_0.func(*str_1)
    var_2 = module_0.func(*list_0)
    module_0.func()


def test_case_1():
    str_0 = "p7waJww\x0c5NGvYDs\nBt5\r"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "?lw&&$*=OIc.{/3i"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    str_1 = "e\\U<}"
    list_0 = [str_1, str_0, str_1]
    var_2 = module_0.func(*list_0)
    module_1.object(**var_1)