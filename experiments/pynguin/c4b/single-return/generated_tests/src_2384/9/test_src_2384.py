# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2384 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xe8N \xbe8"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "1\\7'"
    var_0 = module_0.func(*str_0)
    assert var_0 == "1"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1\\7'"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    assert var_1 == "1"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "j7o`'z:i*WE^Vw\to"
    var_0 = module_0.func(*str_0)
    assert var_0 == "J"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "p~a fay&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "p~a fay&"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "SEY\n{[C"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "sey\n{[c"
    var_1 = module_0.func(*str_0)
    assert var_1 == "s"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "aSMN[5N\r"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Asmn[5n\r"
    var_1 = module_1.object()
    module_0.func()