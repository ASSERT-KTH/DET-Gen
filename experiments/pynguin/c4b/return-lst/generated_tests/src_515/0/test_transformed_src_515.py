# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_515 as module_0


def test_case_0():
    str_0 = "5#+Jda#"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "Ta. \r><57>^x$*u\x0by"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_0)


def test_case_2():
    str_0 = "5#+Jda#"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "C=LECXOVeut/~]LIthG"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()
