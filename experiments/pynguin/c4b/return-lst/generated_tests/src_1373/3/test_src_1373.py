# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1373 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "{"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -1294 - 115.91283j
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [complex_0, tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    complex_0 = 272.93414 - 345.8j
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [complex_0, tuple_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)
