# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2341 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    bytes_0 = b"\x01w\x1eb\xf9\xd7\xe2Q\x8d"
    set_0 = {bool_0, bool_0, bytes_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"q\x15\xb9\xa7\t\tq\xaa\xde\xb1\xb7e\x0e]"
    set_0 = {bool_0, bool_0, bool_0, bytes_0, bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1H=jS: L_cJZR&"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    module_0.func()
