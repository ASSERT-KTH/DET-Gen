# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is True
    bool_1 = False
    module_0.kth(bool_0, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "WDnG24Z6"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.kth(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bytes_0 = b"\xc0"
    module_0.kth(bytes_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.kth(dict_0, bool_0)
    assert var_0 is False
    bytes_0 = b"\x87\xda\xbbcr(6\xc4TD\x8b"
    object_0 = module_0.kth(bytes_0, var_0)
    assert object_0 == 40
    module_0.kth(bytes_0, bytes_0)