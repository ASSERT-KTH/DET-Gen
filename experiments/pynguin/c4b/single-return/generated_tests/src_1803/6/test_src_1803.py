# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1803 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x0eF\xe6UV\x9e\x9cX\x8d\x03\x17\xa4\x149"
    module_0.func(*bytes_0)


def test_case_1():
    str_0 = ":LB?|k^lJTus7 m8dk+s"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    tuple_0 = (dict_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2124
    list_0 = [int_0, int_0, int_0, int_0]
    str_0 = "9I$Mlc61g(iO"
    set_0 = {int_0, int_0, str_0}
    tuple_0 = (list_0, str_0, set_0)
    list_1 = [tuple_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1
    module_0.func()
