# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_487 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "zcu-(nV"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\x84\xe9\xd2]\xb2M-\\"
    list_1 = [bytes_0, bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_2 = module_0.func(*set_0)
    module_0.func()


def test_case_1():
    str_0 = "zcu-(nV"
    int_0 = 1938
    list_0 = [str_0, int_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "t"
    int_0 = 1938
    list_0 = [str_0, int_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "6LSW;q5cwETl}n<"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "c-V"
    int_0 = 1938
    list_0 = [str_0, int_0, str_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\x84\xe9Ya]\xb2M-\\"
    list_1 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_1)
