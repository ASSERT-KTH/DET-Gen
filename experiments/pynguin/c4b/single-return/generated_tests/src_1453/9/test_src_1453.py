# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1453 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xdb\x0c\xd9zj"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 8
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xcbB>\xcc\xcf\xce\xa5\x07iE\x0c\x96\xb6H"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 8
    module_0.func()
