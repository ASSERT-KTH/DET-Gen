# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_954 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    bool_1 = True
    tuple_0 = (bool_0, set_0, bool_1, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "I hate it"
    list_0 = [var_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf7\x82\x11\xdf"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate it"
    )
    module_0.func()
