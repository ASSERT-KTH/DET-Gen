# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_812 as module_0


def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "Sheldon"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb0\xa7\xf7\x9d"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Sheldon"
    bool_0 = True
    module_0.func(*bool_0)
