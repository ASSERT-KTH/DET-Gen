# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1929 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "4PsxY>XV!2"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "b7"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


def test_case_3():
    str_0 = ">99)i|(T{%xcXs\tQyK!"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


def test_case_4():
    str_0 = "480=1xB(amix**$b+Y"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 5
    str_0 = ">99)i|(T{%xcXs\tQyK!"
    list_2 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_2)
    assert var_1 == 8


def test_case_6():
    str_0 = "a4G,"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "a84G,"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    bytes_0 = b"\xcf\x988h\xcaY+\xd6\xe4\x98"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8
    str_0 = "a1G,"
    list_1 = [str_0, str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 3
    module_0.func()


def test_case_9():
    str_0 = "h7wB"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_10():
    bytes_0 = b"\xfc\x0b"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8
    str_0 = "h1"
    list_1 = [str_0, str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_11():
    bytes_0 = b"\xfc\x0b"
    str_0 = "h8^B"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    module_1.object(*bytes_0)
