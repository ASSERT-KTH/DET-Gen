# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1453 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xdaOe\xf7w\x83\xb4\xe13K\x15F\xc0m\x9f\x98?\xd0M"
    var_0 = module_0.func(*bytes_0)
    list_0 = [var_0, var_0, var_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"l\xee\xa0Q\xeb\x81"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
