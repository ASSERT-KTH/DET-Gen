# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2313 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"u"
    int_0 = 675
    bool_0 = True
    list_0 = [bytes_0, bytes_0, int_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "y>%4*"
    var_0 = module_0.func(*str_0)
    module_0.func()
