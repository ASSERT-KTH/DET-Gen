# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_397 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -498
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b" \xbb\x96 \xf8;\x1c2\xe8oJ"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x04\xdeG\x1d\x14\x1b2\xba\x96m?v\xd8A"
    var_0 = module_0.func(*bytes_0)
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    module_0.func()
