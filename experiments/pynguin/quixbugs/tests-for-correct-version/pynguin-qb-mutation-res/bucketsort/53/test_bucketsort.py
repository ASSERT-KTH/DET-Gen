# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "'tFF55sVD'K ."
    module_0.bucketsort(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x18\xf5:\x08\xcb\x1a\xef\x8b\x8f\x95N\x1e\x10\nlH\x93"
    bool_0 = False
    module_0.bucketsort(bytes_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    bool_0 = False
    var_0 = module_0.bucketsort(bytes_0, bool_0)
    module_0.bucketsort(bool_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    bool_0 = True
    var_0 = module_0.bucketsort(bytes_0, bool_0)
    module_0.bucketsort(var_0, var_0)