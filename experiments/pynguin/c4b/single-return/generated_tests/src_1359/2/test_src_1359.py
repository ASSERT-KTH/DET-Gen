# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1359 as module_0


def test_case_0():
    str_0 = "rOf/wa`6MX5<[B&`r:C"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "c8[>kvBu"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "v1et\x0c"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    bytes_0 = b"\xf4\x98\x85j\xa7<\xde"
    list_1 = [bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 8
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "h}w\\!8\t4f\t8\\"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    module_0.func(*var_0)


def test_case_5():
    str_0 = "aDfwrnCho}c87Y*+kG"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "a8Dp/l8:^+u.^yl"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    bytes_0 = b"\xf4/\x98\x85Wj\xa7<\xde"
    list_1 = [bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 8
    module_0.func()
