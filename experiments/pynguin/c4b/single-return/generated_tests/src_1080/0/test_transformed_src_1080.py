# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1080 as module_0


def test_case_0():
    str_0 = "N`n5mSQCg\t'(r>^neHSf"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ";i[j7Dbl0wN{4[iKK"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


def test_case_3():
    str_0 = "KTM0&<lVV6>'$j"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
