# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1504 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    module_0.func(*none_type_0)


def test_case_1():
    str_0 = "7m7y6w*4ynt77\r"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "m7y6w*4ynt77\r"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_3():
    str_0 = "7m7y7,\rw74@nQ77"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
