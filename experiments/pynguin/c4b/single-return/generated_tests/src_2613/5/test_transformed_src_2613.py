# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2613 as module_0


def test_case_0():
    str_0 = "s{Hm[DF=gU)|R#$"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "s{Hm[DF=gU)|R#$"
    bytes_0 = b"W\xf2_\x80\xbf\xc4\xe2\xa9V"
    list_0 = [str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "jCf4Kut\x0co"
    bytes_0 = b"W\xf2_\x80\xbf\xc4\xe2\xa9V"
    list_0 = [str_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "c4*.XVlqd"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bytes_0 = b"W\xf2\xbf\x80K\xc4\xd6\x9fV"
    list_1 = [bytes_0, bytes_0]
#    module_0.func(*list_1)
