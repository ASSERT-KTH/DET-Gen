# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2437 as module_0


def test_case_0():
    bytes_0 = b"\xfc"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_1():
    bytes_0 = b"M_\\\xaf"
    bool_0 = True
    list_0 = [bytes_0, bytes_0, bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(I\x0c)hGXxVx#NZV|C!"
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [str_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
