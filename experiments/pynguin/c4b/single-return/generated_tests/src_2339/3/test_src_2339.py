# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2339 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = []
    dict_0 = {bool_0: bool_0, bool_0: list_0, bool_0: list_0}
    list_1 = [dict_0, dict_0, list_0, bool_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    module_1.object(*var_0, **dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"E\x14A\xef\x1e\xb7\xa71*\xa7"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = []
    dict_0 = {bool_0: bool_0, bool_0: list_0, bool_0: list_0}
    list_1 = []
    list_2 = [list_1, dict_0, list_1]
    module_0.func(*list_2)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "uL}Z=Xxi4;h0aHkM"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    bool_0 = False
    object_0 = module_1.object()
    dict_0 = {bool_0: bool_0, bool_0: object_0, bool_0: object_0}
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"
    var_2 = module_0.func(*list_0)
    assert var_2 == "YES"
    module_1.object(**dict_0)
