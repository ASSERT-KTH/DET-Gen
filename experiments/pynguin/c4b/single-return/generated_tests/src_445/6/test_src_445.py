# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_445 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"{e\xb4\xf60R\xf5$D\xb5\x07eHk\xdd"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x06\x8c\xadQ\x0b\xd0\xd1\xfa3\xdc"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    set_0 = set()
    list_1 = [set_0, set_0, set_0]
    module_0.func(*list_1)
