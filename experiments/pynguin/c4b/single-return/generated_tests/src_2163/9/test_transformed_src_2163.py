# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2163 as module_0


def test_case_0():
    bytes_0 = b"/`\xc9\xf1xh;.\xd8\xd4\xa4\xc0O\xf9{\x1e\xb3\xc4\xeb"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "B&4Ak4m"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "B&4Ak4m"
    list_0 = [str_0, str_0, str_0, str_0]
    list_1 = [list_0, list_0, str_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 3
#    module_0.func()
