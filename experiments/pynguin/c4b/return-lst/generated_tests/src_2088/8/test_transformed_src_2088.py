# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2088 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xe2*\xd2\xa3\x17\xffi\xb74\x1bR\xc6\x19"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"R"
    list_0 = [bytes_0]
    tuple_0 = ()
    list_1 = [list_0, tuple_0, bytes_0, list_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'IDUy;3Zh0oO<|:R"J"'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
#    module_0.func()