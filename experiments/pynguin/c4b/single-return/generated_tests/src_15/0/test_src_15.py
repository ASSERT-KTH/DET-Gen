# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_15 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd3O\x9f\xd4\xe2<j6TP\x1c\xb0\x00\xae.\x0c\x05"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "711111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bool_1 = True
    list_0 = [bool_0, bool_0, bool_1, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bool_1 = True
    list_0 = [bool_0, bool_0, bool_1, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    module_0.func()
