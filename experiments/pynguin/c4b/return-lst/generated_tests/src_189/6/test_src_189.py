# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_189 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "x V,<&5A^?NfiIK"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "^ 7VV,&A^?NiIK"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "xAm=]<yAW?PfIKK"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)