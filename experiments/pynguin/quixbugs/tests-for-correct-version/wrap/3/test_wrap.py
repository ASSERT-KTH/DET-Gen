# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1634.97489
    set_0 = {float_0, float_0}
    var_0 = module_0.wrap(set_0, float_0)
    var_1 = module_0.wrap(set_0, float_0)
    bool_0 = False
    module_0.wrap(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    bytes_0 = b"\x84\xb2b}\xb8^h>,\x02q\xdat|\xd69\xd1\xd8"
    module_0.wrap(bytes_0, bool_0)


def test_case_2():
    str_0 = '~C^4~wK":kjSQ)0\r\t5'
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '~C^4~wK":\\jSQ)0\rW\t '
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)
    tuple_0 = (str_0, str_0, bool_0)
    module_0.wrap(tuple_0, bool_0)
