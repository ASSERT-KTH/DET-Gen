# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1529 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = '}K\rnQ4]93uFI:""0h_'
    var_0 = module_0.func(*str_0)
    assert var_0 == "}"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd5#r\xa2\x90"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "qQl[Fz(\rCTq"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "qQl[Fz(\rCTq"
    var_1 = module_0.func(*var_0)
    assert var_1 == "Q"
    var_2 = module_0.func(*var_1)
    assert var_2 == "q"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\x0c&}V{\\'%"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\x0c&}v{\\'%"
    var_1 = module_1.object()
    module_0.func(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "hA7\r"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Ha7\r"
    str_1 = "qQl[Fz(\rCTq"
    list_1 = [str_1, str_1, str_1, str_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == "qQl[Fz(\rCTq"
    module_0.func()
