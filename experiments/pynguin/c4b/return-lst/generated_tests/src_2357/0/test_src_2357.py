# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2357 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -96
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "DUf4]Ye~~Uu0M b1G*"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc2\x12\xc6\xb6YeG)R\xe4\xa4\xd2,\xa5"
    var_0 = module_0.func(*bytes_0)
    list_0 = [bytes_0]
    list_1 = [list_0]
    module_0.func(*list_1)