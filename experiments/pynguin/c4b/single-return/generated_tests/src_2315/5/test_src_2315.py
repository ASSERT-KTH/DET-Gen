# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2315 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'"c\x08\x10j]?\xd4'
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "?p"
    str_1 = "rB9E3'I<77#aO"
    list_0 = [str_0, str_0, str_0, str_1]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xe1\x8d\xcc"
    list_1 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_1)
