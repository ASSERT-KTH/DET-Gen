# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\n\xbe\xa1\x14UNe"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 127
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "$9P&-"
    bool_0 = False
    tuple_0 = (str_0, bool_0)
    bool_1 = True
    dict_0 = {tuple_0: tuple_0, str_0: str_0, bool_0: bool_1}
    list_0 = [dict_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -807
    bool_0 = False
    list_0 = [bool_0, bool_0]
    bytes_0 = b"\xa2cD Mm"
    tuple_0 = (int_0, bool_0, list_0, bytes_0)
    list_1 = [tuple_0]
    module_0.func(*list_1)
