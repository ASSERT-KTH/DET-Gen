# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_162 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xb7\xd7\xaf\xce!\x08.Z\xb1\x1f\xfet\x89#[\xc9\xd3\xec"
    var_0 = module_0.func(*bytes_0)
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_1.object()
    module_1.object(**var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 626.03438
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    object_0 = module_1.object()
    var_2 = module_0.func(*var_1)
    module_1.object(**var_1)
