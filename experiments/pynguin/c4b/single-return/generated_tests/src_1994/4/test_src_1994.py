# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1994 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xac\xb0\xed\xa6"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
