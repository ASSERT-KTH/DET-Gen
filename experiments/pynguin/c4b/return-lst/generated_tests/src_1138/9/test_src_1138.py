# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1138 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 3304
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"5\n*\xe6\xa1\xcdN\xe9\xc0\xc2\xad\xe5\x01u\x89\x96\x82"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
