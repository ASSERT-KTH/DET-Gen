# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_490 as module_0


def test_case_0():
    str_0 = "@FhFgg`=SIA\nbrK 4o\t"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"H\x9c>\x8d"
#    module_0.func(*bytes_0)


def test_case_2():
    str_0 = "@FhFgg`=SIA\nbrK 4o\t"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_3():
    str_0 = "h%)= AqPe4llo"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


def test_case_4():
    str_0 = "h%)= AqPe4lloT"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
