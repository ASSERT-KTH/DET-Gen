# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_267 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2065
    bytes_0 = b"3]d\r\xd6r\xd4\xa3\t\xfe\xc6>u\x8c\xf9\x87"
    list_0 = [int_0, int_0, bytes_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Rajesh"
    module_0.func()


def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
