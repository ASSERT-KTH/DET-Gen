# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2313 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xc7(T,!}\xad\x9d"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ';P@."eG!\r'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.;.p.@...".g.!.\r'
#    module_0.func()
