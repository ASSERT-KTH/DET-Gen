# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1587 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    object_0 = module_1.object()
    bytes_0 = b"\x9d}\xff\xc60\xe8\xa3P\x94I\x10\xdf\xf4\xf6\xfb\xda\xae"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 10
    module_0.func(*var_0)
