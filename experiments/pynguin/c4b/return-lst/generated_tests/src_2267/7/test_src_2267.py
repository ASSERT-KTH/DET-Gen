# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2267 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"m"
    list_0 = [bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "8~0&U X}"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ".w)~Jo0E!h)p,O4"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "j;0"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*str_0)
    module_0.func()
