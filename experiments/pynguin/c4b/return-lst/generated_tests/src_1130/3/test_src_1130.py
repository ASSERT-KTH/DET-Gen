# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1130 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xc1\xb3\x80\xf4\x934\xb4\xdc\xe5\xed\xf6\x85\x0c_\xe0\x1e"
    dict_0 = {bytes_0: bytes_0}
    module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "V<"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "V<y"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "Vy"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "KK6"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    tuple_0 = (bool_0, list_0)
    list_1 = [tuple_0, bool_0, tuple_0, list_0, bool_0]
    var_0 = module_0.func(*list_1)
    str_0 = "VKK"
    list_2 = [str_0, str_0, var_0]
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_2)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    str_0 = "K"
    tuple_0 = (bool_0, str_0)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    bool_1 = False
    var_1 = module_0.func(*var_0)
    str_1 = "YVV\t"
    list_1 = [str_1, str_1, bool_1]
    var_2 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = False
    str_0 = "KV"
    tuple_0 = (bool_0, str_0)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    bool_1 = False
    var_1 = module_0.func(*var_0)
    str_1 = 'V"H'
    list_1 = [str_1, str_1, bool_1]
    var_2 = module_0.func(*list_1)
    module_0.func()
