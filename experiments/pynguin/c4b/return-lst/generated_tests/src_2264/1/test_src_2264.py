# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2264 as module_0


def test_case_0():
    str_0 = "\n`!="
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "\n`!=z7"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "5V?0\\4FE|MH7*\\1\t77,"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4Qo\\4FE|MH77*\\447"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()