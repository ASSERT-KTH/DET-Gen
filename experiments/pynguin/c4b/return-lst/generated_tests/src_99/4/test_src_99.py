# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_99 as module_0


def test_case_0():
    str_0 = "1-QIGMw"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "1-QIGMw"
    var_0 = module_0.func(*str_0)
    bytes_0 = b"\x9c\xa8\xb7\x04l"
    var_1 = module_0.func(*bytes_0)
    module_0.func()
