# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2437 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


def test_case_1():
    str_0 = 'UX%\x0bLb5=\x0c/B\x0b"'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*str_0)
    assert var_1 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "`q/_EKDNVn!8\tQ"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
