# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1820 as module_0


def test_case_0():
    bytes_0 = b"\xf3\x19\xb0\x9c\xcfa\t\x17Xq*"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\\\xb5}i\xec\xab\xcdN\x11\xc8\x8d\xb5\xa4\x83\xacW\xb9\x1a"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 7
    tuple_0 = ()
    list_0 = [int_0, int_0, tuple_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()