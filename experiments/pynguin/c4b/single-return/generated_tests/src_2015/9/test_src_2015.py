# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2015 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    module_1.object(**var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"g\x1c\x9e"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 98
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_1.object(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xaf\xda@|\xc5\xed\xfb\xf4\x19\xa6\xe9\xe4\x85J+\x86"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 112
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    float_0 = 1330.264404
    list_0 = [bool_0, float_0, bool_0, float_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bool_1 = False
    list_1 = [bool_1, bool_1, bool_1, bool_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
    module_1.object(*bool_0)
