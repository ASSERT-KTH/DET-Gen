# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_466 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "8r\n5;;qFyFIYf$k_[kAv"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0>=S!Zt<)6\\\x0c>p"
    var_0 = module_0.func(*str_0)
    assert var_0 == "0"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "81)5;;qFyFIYf+kk[kAv"
    module_0.func(*str_0)
