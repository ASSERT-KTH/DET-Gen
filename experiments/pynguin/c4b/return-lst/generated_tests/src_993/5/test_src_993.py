# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_993 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x8b\xea\x8dy\x16\x93c\xa8"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bool_1 = True
    bool_2 = False
    tuple_0 = (bool_0, bool_1, bool_2, bool_2)
    list_0 = [bool_0, tuple_0, tuple_0, bool_2]
    var_0 = module_0.func(*list_0)
    module_0.func()
