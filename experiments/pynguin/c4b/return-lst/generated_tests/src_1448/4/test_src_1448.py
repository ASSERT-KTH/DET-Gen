# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1448 as module_0


def test_case_0():
    complex_0 = -81.1164 + 1042.57j
    tuple_0 = (complex_0,)
    list_0 = [tuple_0, complex_0, tuple_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = 'nAk"@!>/4:\r#h'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "hlelloS"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
