# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_427 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x12\xbe "
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "W[$5W@BLWgC?"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "j\\gR0uRLRf\\Yo"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 12
    module_0.func()
