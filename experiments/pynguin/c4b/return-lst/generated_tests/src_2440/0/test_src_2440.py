# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2440 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x1d\xb4\xe6a\xc0\xe2\xcdf\x06X"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1d\xb4\xe6a\xc0\xe2\xcdf\x06X"
    str_0 = "KO"
    var_0 = module_0.func(*str_0)
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x1d\xb4\xe6a\xc0\xe2\xcdf\x06X"
    str_0 = "KO"
    list_0 = [str_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, bytes_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x1d\xb4\xe6a\xe2\xcd\x06"
    str_0 = "KO"
    list_0 = [str_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "RaQT|P"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x1d\xb4\xe6a\xc0\xe2\xcdf\x06X"
    str_0 = "KO"
    list_0 = [str_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, bytes_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"\x1d\xb4\xe6a\xc0\xe2\xcdf\x06X"
    str_0 = ")C"
    list_0 = [str_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, bytes_0]
    module_0.func(*list_1)
