# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1937 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Okl"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Okl"
    object_0 = module_0.func(*str_0)
    assert object_0 == "o"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"(\x05A\x11\x93\xd5"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "vwN6<\n"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "vwN6<\n"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "kT"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Kt"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "TJ"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "tj"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "kT"
    var_0 = module_0.func(*str_0)
    assert var_0 == "K"
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "Kt"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "_Z"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "_Z"
    module_1.object(**var_0)
